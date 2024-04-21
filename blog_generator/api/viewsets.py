from pytube import YouTube
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import assemblyai as aai
from django.conf import settings
import environ
from ..models import Blog
from rest_framework.exceptions import NotAuthenticated
import os


env = environ.Env()
env.read_env()


import requests



@api_view(["POST"])
def blog_generator(request):


    if not request.user.is_authenticated:
        raise NotAuthenticated

    url = request.data["link"]
    # get video object by pytube
    video_obj = YouTube(url)

    # get transcribed text
    (transcribed_text , audio_path) = transcribe(video_obj)
    
    prompt = f"Based on the following transcript from a YouTube video, write a comprehensive blog article, write it based on the transcript, but dont make it look like a youtube video, make it look like a proper blog article:\n\n{transcribed_text}\n\n"


    blog = generate_blog(prompt)

    data = {
        "title": video_obj.title,
        "body": blog
    }

    blogInstance = Blog(owner=request.user , title=video_obj.title , body=blog)
    blogInstance.save()

    os.remove(audio_path)

    
    return Response(data , status=status.HTTP_200_OK)

def download_audio(video):
    audio = video.streams.filter(only_audio=True).first()
    audio_path = audio.download(settings.MEDIA_ROOT)
    return audio_path

def transcribe(video):
    aai.settings.api_key = env("AAI_APIKEY")
    audio_path = download_audio(video)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path)
    transcribed_text = transcript.text
    return (transcribed_text , audio_path)

def generate_blog(prompt):
    url = "https://api.edenai.run/v2/text/generation"

    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "temperature": 0,
        "max_tokens": 1000,
        "text": prompt,
        "providers": "google"
    }
    headers = {
        "Authorization": f'Bearer {env("EDEN_APIKEY")}',
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()["google"]["generated_text"]
from pytube import YouTube
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import assemblyai as aai
from django.conf import settings
import environ

env = environ.Env()
env.read_env()

@api_view(["POST"])
def generate_blog(request):

    url = request.data["link"]
    # get video object by pytube
    video_obj = YouTube(url)

    # get transcribed text
    transcirbed_text = transcribe(video_obj)
    
    res = {
        "title": video_obj.title,
        "body": transcirbed_text
    }
    return Response(res , status=status.HTTP_200_OK)

def download_audio(video):
    audio = video.streams.filter(only_audio=True).first()
    audio_path = audio.download(settings.MEDIA_ROOT)
    return audio_path

def transcribe(video):
    aai.settings.api_key = env("AAI_APIKEY")
    audio_path = download_audio(video)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path)
    print(transcript.text)
    return transcript.text
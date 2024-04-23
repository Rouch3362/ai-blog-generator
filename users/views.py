from django.shortcuts import render , redirect, get_object_or_404
from .forms import RegisterUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic import DetailView

# Create your views here.
def RegisterUser(request):
    if request.method == "POST":
        r_form = RegisterUserForm(request.POST)

        if r_form.is_valid():
            user = r_form.save()
            login(request , user)
            messages.success(request , "Your Account Created And Now You Are Logged In")
            return redirect("home")
    else:
        r_form = RegisterUserForm()

    return render(request , "register.html" , {"form": r_form})


def single_user(request , username):    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User Not Found")
        
    return render(request , "single-user.html" , {"user": user})
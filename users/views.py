from django.shortcuts import render , redirect
from .forms import RegisterUserForm
from django.contrib.auth import login
from django.contrib import messages
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

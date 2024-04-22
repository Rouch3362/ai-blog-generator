from django.shortcuts import render , redirect
from .api.viewsets import main_func
from django.contrib import messages
# Create your views here.

def home(request):
    
    if request.method == "POST":
        url = request.POST.get("link")

        if url is None:
            messages.error(request , "Link Is Required")
            return redirect("home")

        if not request.user.is_authenticated:
            messages.error(request , "Login To Your Account To Use Blog Generator")
            return
        
        data = main_func(url , request.user)

        return render(request , "home.html" , {"data": data})
        
        
    else:
        return render(request , "home.html")
from django.shortcuts import render , redirect
from .api.viewsets import main_func
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
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
    
class Blogs(ListView , LoginRequiredMixin):
    model = Blog
    template_name = "blogs.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user).order_by("-createdAt")
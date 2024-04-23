from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from .api.viewsets import main_func , is_link_valid
from django.contrib import messages
from django.views.generic import ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from django.http import Http404
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
        
        # checks if the link is youtube link
        if not is_link_valid(url):
            messages.error(request , "Please Enter A Valid Youtube Link")
            return redirect("home")
        
        data = main_func(url , request.user)

        return render(request , "home.html" , {"data": data})
        
        
    else:
        return render(request , "home.html")
    
class Blogs(ListView , LoginRequiredMixin):
    model = Blog
    template_name = "blogs.html"
    context_object_name = "blogs"
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user).order_by("-createdAt")
    
def single_blog(request , pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        raise Http404("Blog Not Found")
    
    return render(request , "single-blog.html" , {"blog": blog})
    
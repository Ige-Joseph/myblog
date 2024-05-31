from django.shortcuts import render
from .models import myBlogDdDefined
# Create your views here.

def index(request):
    posts = myBlogDdDefined.objects.all()
    
    return render(request, 'index.html', {'posts': posts})


def posts(request, pk):
    Post = myBlogDdDefined.objects.get(id=pk)
    
    return render(request, 'posts.html', {'post': Post})
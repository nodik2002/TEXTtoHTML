from django.shortcuts import render
from .models import Post,Image
from blog.forms import PostForm
from django.http import HttpResponse

def home(request):
    form=PostForm()
    return render(request,'blog/home.html',{'form':form})

def blog(request):
    blogs = Post.objects.all()
    return render(request,'blog/blog.html',{'blogs':blogs})

def image(request,slug):
    image = Image.objects.get(slug=slug)
    return HttpResponse(image.image, content_type="image/jpg")

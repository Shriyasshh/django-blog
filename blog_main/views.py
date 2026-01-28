from django.shortcuts import render
from blogs.models import Category,Blog

def  home(request):
    featured = Blog.objects.filter(is_featured=True, status = 'published').order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False , status = 'published').order_by('-created_at')


    context = {
       'featured':featured,
       'posts':posts
               }
    return render(request, "home.html",context)
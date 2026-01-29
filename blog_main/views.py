from django.shortcuts import render
from blogs.models import Category,Blog
from assignment.models import About

def  home(request):
    featured = Blog.objects.filter(is_featured=True, status = 'published').order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False , status = 'published').order_by('-created_at')
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
       'featured':featured,
       'posts':posts,
       'about':about
               }
    return render(request , 'home.html', context)
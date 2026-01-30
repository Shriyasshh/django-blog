from django.shortcuts import render,redirect
from blogs.models import Blog
from assignment.models import About
from .forms import SignInForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login

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

def signin(request):

    if request.method =='POST':
        form =SignInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:    
        form =SignInForm()
    context={
        'form':form
    }
    return render(request, 'signin.html',context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
        }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')
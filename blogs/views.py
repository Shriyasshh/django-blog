# from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import Blog,Category
from django.shortcuts import get_object_or_404


# Create your views here.

def posts_by_category(request,category_id):
    post = Blog.objects.filter(status='published',category = category_id).order_by('-created_at')
    
    """ Passing Category object name to template 
        get-object-or-404 when want to show 404 page """
    category = get_object_or_404(Category, pk=category_id)
    """  or  when want to redirect to other page"""
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except :
    #     return redirect('home')
    
    context = {
        'category': category,
        'post':post
    }
    return render(request,'post_by_category.html',context)
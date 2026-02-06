# from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import Blog,Category,Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q


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


def blogs(request ,slug):
    single_blog = get_object_or_404(Blog, slug=slug,status ='published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return redirect('blogs',slug=slug)
    # Comments
    comments = Comment.objects.filter(blog = single_blog)
    comment_count = comments.count()
    context = {
        'single_blog':single_blog,
        'comments':comments,
        'comment_count':comment_count
    }
    return render(request ,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    if keyword:
        blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status ='published').order_by('-created_at')
        print(blogs)
        context = {
            "keyword":keyword,
            "blogs":blogs,
        }

    return render(request, 'search.html',context)
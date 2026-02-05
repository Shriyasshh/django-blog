from django.shortcuts import get_object_or_404, render,redirect
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogPostForm
from django.template.defaultfilters import slugify

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count  = Blog.objects.all().count()
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count
    }
    return render(request , 'dashboard/dashboard.html',context)

@login_required(login_url='login')
def categories(request):
    return render(request , 'dashboard/categories.html')

@login_required(login_url='login')
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context= {
        'form':form
    }
    return render(request , 'dashboard/add_category.html',context)

@login_required(login_url='login')
def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    
    context= {
        'form':form,
        'category':category,
    }
    return render(request , 'dashboard/edit_category.html',context)

@login_required(login_url='login')
def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all().order_by('-created_at')
    context = {
        'posts':posts
    }
    return render(request , 'dashboard/posts.html',context)

@login_required(login_url='login')
def add_posts(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post =form.save(commit=False) #tempory save form
            post.author = request.user
            post.save()
            post.slug = slugify(post.title) + '-'+ str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = BlogPostForm()
    context= {
        'form':form,
    }
    return render(request , 'dashboard/add_posts.html',context)


@login_required(login_url='login')
def edit_posts(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title) + '-'+ str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = BlogPostForm(instance=post)
    
    context= {
        'form':form,
        'post':post,
    }
    return render(request , 'dashboard/edit_posts.html',context)

@login_required(login_url='login')
def delete_posts(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')
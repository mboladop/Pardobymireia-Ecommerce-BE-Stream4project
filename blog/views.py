from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Blog
from .forms import BlogPostForm
from django.http import HttpResponseForbidden

def get_blogs(request):
    blogs = Blog.objects.all()
    
    return render(request, "blog/blog.html", {'blogs': blogs})
    
def delete_blog(request, pk):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=pk)
        try:
            blog.delete()
            messages.success(request, 'Has eliminado el blog')
        except:
            messages.warning(request, 'No has eliminado el blog')
    return redirect('get_blogs')
    
def liked_blogs(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(likes=request.user)
    else:
        blogs = Blog.objects.all()
    
    return render(request, "accounts/profile.html", {'blogs': blogs})
    
def blog_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    blog = get_object_or_404(Blog, pk=pk)
    blog.views += 1
    blog.save()
    return render(request, "blog/blogdetail.html", {'blog': blog})

def new_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', blog.pk)
    else:
        form = BlogPostForm()
        
    return render(request, 'blog/blogform.html', {'form': form})
        
        
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if request.method == "POST":
        form = BlogPostForm(request.BLOG, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', blog.pk)        
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'blog/blogform.html', {'form': form})
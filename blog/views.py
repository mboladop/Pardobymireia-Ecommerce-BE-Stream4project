from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogPostForm
from django.http import HttpResponseForbidden

def get_blogs(request):
    blogs = Blog.objects.all()
    
    return render(request, "blog/blog.html", {'blogs': blogs})
    
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
    blog = get_object_or_404(Post, pk=pk)
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
            return redirect('blogdetail', blog.pk)
    else:
        form = BlogPostForm()
        
    return render(request, 'blog/blogform.html', {'blog': blog})
        
        
def edit_blog(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = BlogPostForm(request.BLOG, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blogdetail', blog.pk)        
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'blogs/blogform.html', {'blog': blog})
from django.shortcuts import render
from .models import Post, Author

def post_list(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    return render(request, 'tangram_blog/home.html', {'posts': posts, 'authors': authors})
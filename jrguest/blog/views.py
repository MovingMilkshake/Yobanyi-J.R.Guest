from django.shortcuts import render

# Create your views here.
from blog.models import Posts


def get_posts():
    return Posts.objects.all()


def index_page(request):
    context = {
        'posts': get_posts()
    }
    return render(request, 'index.html', context)


def blog_page(request):
    context = {
        'posts': get_posts()
    }
    return render(request, 'blog.html', context)


def about_page(request):
    return render(request, 'about.html')

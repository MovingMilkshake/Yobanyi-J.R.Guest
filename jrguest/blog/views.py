from django.shortcuts import render

# Create your views here.


def index_page(request):
    return render(request, 'index.html')


def blog_page(request):
    return render(request, 'blog.html')


def about_page(request):
    return render(request, 'about.html')

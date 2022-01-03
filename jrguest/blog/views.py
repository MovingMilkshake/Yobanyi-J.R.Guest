from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from blog.models import Posts
from blog.forms import PostForm


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


def create_post_page(request):
    context = {}

    if request.method == 'POST':
        form = PostForm(request.POST)
        a = form.data['title']
        b = form.data['description']
        record = Posts(title=a, description=b, date=timezone.now())
        record.save()
        context['form'] = form
    elif request.method == 'GET':
        context['form'] = PostForm()

    return render(request, 'createpost.html', context)


def about_page(request):
    return render(request, 'about.html')

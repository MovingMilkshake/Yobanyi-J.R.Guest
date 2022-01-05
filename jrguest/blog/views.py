from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Post
from .forms import PostForm


class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class PostView(DetailView):
    model = Post
    template_name = 'post.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'createpost.html'


class AboutView(TemplateView):
    template_name = 'about.html'

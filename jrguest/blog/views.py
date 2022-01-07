from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm


class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


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


class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'editpost.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('index_page')


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'newcategory.html'

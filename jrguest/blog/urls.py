from django.urls import path
from .views import IndexView, BlogView, PostView, CreatePostView, AboutView, EditPostView, DeletePostView


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('blog/', BlogView.as_view(), name='blog_page'),
    path('blog/<int:pk>', PostView.as_view(), name='post_page'),
    path('blog/create/', CreatePostView.as_view(), name='create_post_page'),
    path('blog/edit/<int:pk>', EditPostView.as_view(), name='edit_post_page'),
    path('blog/delete/<int:pk>', DeletePostView.as_view(), name='delete_post_page'),
]

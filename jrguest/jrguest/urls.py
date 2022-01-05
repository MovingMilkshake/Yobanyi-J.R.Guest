"""jrguest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from blog.views import IndexView, BlogView, PostView, CreatePostView, AboutView, EditPostView, DeletePostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('blog/', BlogView.as_view(), name='blog_page'),
    path('blog/<int:pk>', PostView.as_view(), name='post_page'),
    path('blog/create/', CreatePostView.as_view(), name='create_post_page'),
    path('blog/edit/<int:pk>', EditPostView.as_view(), name='edit_post_page'),
    path('blog/delete/<int:pk>', DeletePostView.as_view(), name='delete_post_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('title', 'title')
choice_list = [choice for choice in choices]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'description', 'text', 'thumbnail')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter text here',
                                            'class': 'title-input'}),
            'category': forms.Select(choices=choice_list),
            'description': forms.Textarea(attrs={'placeholder': 'Enter text here, but a little longer'}),
            'text': forms.Textarea(attrs={'placeholder': 'Enter text here, but big'}),
            'thumbnail': forms.FileInput(),
        }

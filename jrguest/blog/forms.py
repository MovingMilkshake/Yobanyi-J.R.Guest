from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'text', 'thumbnail')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter text here',
                                            'class': 'form-input title-input'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter text here, but a little longer',
                                                 'class': 'form-input'}),
            'text': forms.Textarea(attrs={'placeholder': 'Enter text here, but big',
                                          'class': 'form-input'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-input'}),
        }

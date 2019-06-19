from django import forms
from .models import Post
from .choices import *

class PostForm(forms.ModelForm):
    category = forms.ChoiceField(choices=PRIVACY_CHOICES)
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'image',]
        
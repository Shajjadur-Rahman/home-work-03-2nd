from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'post_img', 'post_content']

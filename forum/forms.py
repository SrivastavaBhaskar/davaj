from django import forms
from forum.models import Thread, Post


class CreateThread(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
from django import forms
from SportBlog.models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'description', 'fecha', 'hora', 'image', 'lugar']
        exclude = ['user']
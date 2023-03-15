from .models import Comment
from django import forms 
from .models import mba


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = PostForm
        fields = ['featured_image', 'title', 'price', 'content', 'created_on']
        widgets = {
           'featured_image' : forms.ImageField(attr={'class': 'form-control'}),
           'title' : forms.TextInput(attr={'class': 'form-control'}),
           'price' : forms.DecimalField(attr={'class': 'form-control'}),
           'content' : forms.TextInput(attr={'class': 'form-control'}),
           'created_on' : forms.DateTimeField(attr={'class': 'form-control'}),
        }
      
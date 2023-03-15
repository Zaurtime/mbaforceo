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
           'featured_image' : forms.ImageField(attrs={'class': 'form-control'}),
           'title' : forms.TextInput(attrs={'class': 'form-control'}),
           'price' : forms.DecimalField(attrs={'class': 'form-control'}),
           'content' : forms.TextInput(attrs={'class': 'form-control'}),
           'created_on' : forms.DateTimeField(attrs={'class': 'form-control'}),
        }
      
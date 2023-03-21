from .models import Comment
from django import forms 
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['featured_image', 'title', 'content', ]
        widgets = {
           'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           'content': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['featured_image', 'title', 'content', ]
      
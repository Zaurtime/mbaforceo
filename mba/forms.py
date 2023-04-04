from .models import Comment
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "featured_image",
            "title",
            "content",
        ]
        widgets = {
            "featured_image": forms.FileInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "featured_image",
            "title",
            "content",
        ]


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "required": "",
                "name": "username",
                "type": "text",
                "class": "form-input",
                "placeholder": "mba for ceo",
                "maxlength": "16",
                "minlength": "6",
            }
        )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]
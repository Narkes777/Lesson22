from django.forms import ModelForm

from .models import Post, Author


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


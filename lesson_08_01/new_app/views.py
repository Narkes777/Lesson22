from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Post


class PostList(ListView):
    model = Post
    # context_object_name = 'object_list'

    def get_queryset(self):
        get_params = self.request.GET


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post_list')


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post_list')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'new_app/post_form.html'


class About(TemplateView):
    template_name = 'about.html'

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


class MainPage(TemplateView):
    template_name = 'new_app/about.html'

    class Example:

        def __init__(self):
            self.param = 42

        def get_param(self):
            return self.param + 100

    def get_context_data(self, **kwargs):

        def func():
            return 100

        context = super().get_context_data(**kwargs)
        a = func
        b = [1, 2, 3, 4]
        context['var'] = a
        context['b'] = b
        # new_context = {'var': a}
        # context.update(new_context)
        return context




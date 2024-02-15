from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post


class PostList(ListView):
    model = Post
    # context_object_name = 'object_list'


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page": page}
    return render(request, "new_app/post_list.html", context)


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     b = [1, 1, 1, 2, 3, 3, 3, 4, 4, 5]
    #     list_of_booleans = [True, False, True, None]
    #     c = Post.objects.last()
    #     condition = 10
    #     number = 34.123131
    #     context['b'] = b
    #     context['post'] = c
    #     context['condition'] = condition
    #     context['boolean_list'] = list_of_booleans
    #     context['number'] = number
    #     # new_context = {'var': a}
    #     # context.update(new_context)
    #     return context



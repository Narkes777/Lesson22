from django.shortcuts import render
from .models import Post, Category, Author
from .forms import PostForm, AuthorForm
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.template.loader import get_template
from django.views.generic import UpdateView

from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic.base import ContextMixin, TemplateResponseMixin, TemplateView
from django.views.generic.detail import SingleObjectMixin, SingleObjectTemplateResponseMixin, DetailView
from django.views.generic.list import MultipleObjectMixin, MultipleObjectTemplateResponseMixin, ListView

# ContextMixin
# extra_content
# get_context_data(**kwargs)


def author_list(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all() #[]
    context = {'author_list': authors}
    return render(request, 'new_app/author_list.html', context=context)


# class AuthorList(View, ContextMixin, TemplateResponseMixin):
#     template_name = 'author_list.html'
#     http_method_names = ['post', 'get']
#
#     # 'get'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['author_list'] = Author.objects.all()
#         return context
#
#     def get(self, request: HttpRequest) -> HttpResponse:
#         return self.render_to_response(self.get_context_data())


# class AuthorList(TemplateView):
#     template_name = 'new_app/author_list.html'
#
#     def get_context_data(self, **kwargs):
#         return {'author_list': Author.objects.all()}

# class AuthorList(View, MultipleObjectMixin, MultipleObjectTemplateResponseMixin):
#     model = Author
#     template_name = 'author_list.html'
#     context_object_name = 'author_list'
#
#     def get(self, *args, **kwargs):
#         self.object_list = self.get_queryset()
#         context = self.get_context_data()
#         return self.render_to_response(context)


class AuthorList(ListView):
    model = Author
    context_object_name = 'author_list'




class CategoryList(ListView):
    model = Category
    context_object_name = 'category_list'


# class AuthorDetail(View, SingleObjectMixin, SingleObjectTemplateResponseMixin):
#     model = Author
#     pk_url_kwarg = 'pk'
#     template_name = 'author_detail.html'
#     context_object_name = 'author'
#
#     def get(self, request: HttpRequest, pk: int) -> HttpResponse:
#         self.object = self.get_object() # Author.objects.get(pk=pk)
#         return self.render_to_response(self.get_context_data())


class AuthorDetail(DetailView): # DetailView = View + SingleObjectMixin + SingleObjectTemplateResponseMixin + get()
    model = Author


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) # context = {'object': self.get_object()}
    #     context['extra_context'] = "Author random string"
    #     context['random_string'] = 'dadawdawfrawfaw'
    #     return context



# model - аттрибут модели, в которой происходит поиск
# pk_url_kwarg -
#
# class AuthorDetail(View, SingleObjectMixin):
#     model = Author # NOT get()
#     pk_url_kwarg = 'pk' # not get
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object() # self.model.objects.get(pk=kwargs[self.pk_url_kwarg])
#         return HttpResponse(self.object)
#

# __call__()
# as_view()
# dispatch(request, **kwargs)

# Формы:
# 1) Формы, связанные с моделью - save()
# 2) Формы, не связанные с моделью -

# Factory method


from django.forms import modelform_factory


author_form = modelform_factory(Author, fields='__all__')

# FormView
from django.views.generic.edit import FormMixin, TemplateResponseMixin
# form_class = author_form
# initial
# success_url
# get_context_data
# form_valid()
# form_invalid()

from django.views.generic.edit import ProcessFormView
from django.urls import reverse_lazy


# class CreateFormView(ProcessFormView, FormMixin, TemplateResponseMixin):
#     form_class = author_form
#     template_name = 'new_app/author_form.html'
#     initial = {'name': "Укажите имя автора"}
#     success_url = reverse_lazy('author_list') # 'authors/'
#
#     def form_valid(self, form):
#         form.save()
#         return HttpResponse('new author saved')
#
#     def form_invalid(self, form):
#         return HttpResponse('Error when saving new author')


from django.views.generic.edit import FormView


# class CreateFormView(FormView):
#     form_class = modelform_factory(Author, fields='__all__')
#     template_name = 'new_app/author_form.html'
#     success_url = reverse_lazy('author_list')
#
#     def form_valid(self, form):
#         form.save()
#         return HttpResponse('new author saved')
#
#     def form_invalid(self, form):
#         return HttpResponse('Error when saving new author')


from django.views.generic.edit import CreateView


class CreateFormView(CreateView):
    model = Author
    template_name = 'new_app/author_form.html'
    fields = '__all__'
    success_url = reverse_lazy('author_list')


def post_get_form(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = request.POST
        form = PostForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Successfully saved new post</h1>')
        else:
            return HttpResponse('Invalid data', )
    else:
        form = PostForm()
        context = {'form': form, "model_name": "Post"}
        return render(request, 'form.html', context)

# request.POST - словарь
# request.GET - словарь
# request.FILES
# request.method
# request.body
# request.headers



# def post_post_form(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         data = request.POST
#         form = PostForm(data)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Successfully saved new post')
#         else:
#             return HttpResponse('Invalid data')
#     else:
#         return HttpResponse(status=405)


def get_published_posts(request: HttpRequest) -> HttpResponse:
    filtered_status = request.GET.get('status', None)
    posts = Post.objects.filter(status=filtered_status)
    template = get_template('published_post_list.html')
    context = {"post_list": posts}
    return HttpResponse(template.render(request=request, context=context))


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    l = []
    result = ''
    for elem in l:
        result += elem
    res = HttpResponse(result)
    return res


def category_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return HttpResponse(categories)


def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    category = Category.objects.get(pk=pk)
    #1
    posts = Post.objects.filter(categories=category)
    #2
    posts = category.post_set.all()
    result = ''
    for post in posts:
        result += str(post)
    result += category.name
    return HttpResponse(result)

    # try:
    #     post = Post.objects.get(pk=pk)
    #     return HttpResponse(post.author_id.name)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound(f'Объект с ключем {pk} не был найден')





def author_detail(request: HttpRequest, pk: int) -> HttpResponse:
    author = get_object_or_404(Author, pk=pk)
    context = {'author': author}
    return render(request, 'author_detail.html', context=context)


def author_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = request.POST
        form = AuthorForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse('New author has been saved', status=201)
        else:
            return HttpResponse('Error when saving new author', status=400)
    else:
        form = AuthorForm()
        return render(request, 'form.html', {'form': form, "model_name": "Author"})


def author_update(request: HttpRequest, pk: int) -> HttpResponse:
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        data = request.POST
        form = AuthorForm(data, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', pk=author.pk)
        else:
            return HttpResponse('Error when saving new author', status=400)
    else:
        form = AuthorForm(instance=author)
        return render(request, 'form.html', {'form': form, "model_name": "Author"})


class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'form.html'
    fields = '__all__'


def author_delete(request: HttpRequest, pk: int) -> HttpResponse:
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return HttpResponse(f"Author with pk {author.pk} has been deleted")
    return render(request, "form.html", {"model_name": "Author", "action": "Delete"})

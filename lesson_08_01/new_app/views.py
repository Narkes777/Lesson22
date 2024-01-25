from django.shortcuts import render
from .models import Post, Category
from .forms import PostForm
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.template.loader import get_template

from django.shortcuts import get_object_or_404, render

# Create your views here.


def post_get_form(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = request.POST
        form = PostForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully saved new post')
        else:
            return HttpResponse('Invalid data')
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'form.html', context)


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


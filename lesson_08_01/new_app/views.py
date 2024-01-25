from django.shortcuts import render
from .models import Post, Category, Author
from .forms import PostForm, AuthorForm
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.template.loader import get_template
from django.views.generic import UpdateView

from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.


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


def author_list(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()
    context = {'author_list': authors}
    return render(request, 'author_list.html', context=context)


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

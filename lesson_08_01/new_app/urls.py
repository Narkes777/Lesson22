from .views import AuthorDetail, CreateFormView, post_detail, AuthorList, post_get_form, author_list, author_detail, author_create, AuthorUpdate, author_update, author_delete
from django.urls import path

urlpatterns = [
    path('<int:pk>/', AuthorDetail.as_view(), name='post_detail'),
    path('posts/', AuthorList.as_view(), name='published_posts'),
    path('posts/create/', post_get_form, name='post_get_form'),

    path('authors/', author_list, name='author_list'),
    path('authors/<int:pk>/', author_detail, name='author_detail'),
    path('authors/create/', CreateFormView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdate.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', author_delete, name="author_delete")
]


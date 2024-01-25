from .views import post_detail, get_published_posts, post_get_form
from django.urls import path

urlpatterns = [
    path('<int:pk>/', post_detail, name='post_detail'),
    path('posts/', get_published_posts, name='published_posts'),
    path('posts/create/', post_get_form, name='post_get_form'),
]


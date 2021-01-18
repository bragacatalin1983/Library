
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('posts/<int:pk_id>', views.posts, name='posts'),
    path('desprenoi/', views.desprenoi, name='desprenoi'),
    path('like/', views.blog_likes, name='blog_likes'),
]

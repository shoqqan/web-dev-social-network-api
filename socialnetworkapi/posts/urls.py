from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/<int:post_id>/comments/', views.comment_list, name='comment-list'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', views.comment_detail, name='comment-detail'),
]

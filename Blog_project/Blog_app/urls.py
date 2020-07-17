from django.urls import path
from . import views

app_name = 'Blog_app'

urlpatterns = [
    path('', views.home, name='home'),
    # path('create-author/', views.create_author, name='create-author'),
    path('recent-posts/', views.recent_posts, name='recent-posts'),
    path('posts-detail/<int:post_id>', views.detail_post, name='posts-detail'),
    path('posts-under-category/<int:cat_id>', views.posts_under_category, name='posts-under-category'),
    path('create-post/', views.create_post, name='create-post'),
    path('create-category/', views.create_category, name='create-category'),
]
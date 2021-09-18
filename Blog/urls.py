from django.urls import path

from Blog.views import show_all_posts, show_post

urlpatterns = [
    path('posts', show_all_posts),
    path('posts/<int:post_id>', show_post)
]
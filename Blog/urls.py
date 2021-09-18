from django.urls import path

from Blog.views import show_all_posts, show_post

urlpatterns = [
    path('', show_all_posts),
    path('<int:post_id>', show_post)
]
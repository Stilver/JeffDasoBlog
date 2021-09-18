from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from Blog.models import Post


def show_all_posts(request):
    return render(request, '../templates/posts.html', {'posts': Post.objects.all()[::-1]})


def show_post(request, post_id):
    post = Post.objects.filter(id=post_id)
    if post:
        post.watch_count += 1
        post.save()
        return render(request, '../templates/current_post.html', {'post': post.first()})
    return HttpResponseNotFound(f"Post not found")

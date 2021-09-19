from django.http import HttpResponseNotFound
from django.shortcuts import render

from Blog.models import Post


def show_all_posts(request):
    prepared_posts = []
    for post in Post.objects.all():
        prepared_posts.append(prepare_post_for_publication(post, preview=True))
    return render(request, '../templates/posts.html', {'posts': prepared_posts})


def show_post(request, post_id):
    post = Post.objects.filter(id=post_id)

    if not post:
        return HttpResponseNotFound(f"Post not found")

    post = post.first()
    post.watch_count += 1
    post.save()

    prepared_post = prepare_post_for_publication(post)
    return render(request, '../templates/current_post.html', {'post': prepared_post})


def prepare_post_for_publication(post: Post, preview: bool = False):
    result = {'id': post.id, 'title': post.title}

    content = post.content
    if preview:
        # todo add pics to posts
        if len(content) > 200:
            content = content[:200] + '...'
    result['content'] = content

    result['publication_date'] = post.publication_date

    return result

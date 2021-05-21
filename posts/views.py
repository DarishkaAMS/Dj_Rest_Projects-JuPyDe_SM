from django.http import Http404, JsonResponse
from django.shortcuts import render

from .models import Post


# Create your views here.


def post_list_view(requests, *args, **kwargs):
    query_set = Post.objects.all()
    post_list = [{"id": post.id, "title": post.title, "slug": post.slug, "content": post.content,
                  "upload_date": post.upload_date} for post in query_set]
    data = {
        "response": post_list
    }

    return JsonResponse(data)


def post_detail_view(request, post_id, *args, **kwargs):
    data = {
        "id": post_id,
    }
    status = 200
    try:
        obj = Post.objects.get(id=post_id)
        data['title'] = obj.title,
        data['slug'] = obj.slug,
        data['content'] = obj.content,
        data['upload_date'] = obj.upload_date,
    except:
        data['message'] = f"Oops... I have not found {post_id}"
        status = 200

    return JsonResponse(data, status=status)

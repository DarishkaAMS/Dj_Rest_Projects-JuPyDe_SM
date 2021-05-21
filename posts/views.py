from django.http import Http404, JsonResponse
from django.shortcuts import render

from .models import Post
# Create your views here.


def post_detail_view(request, post_id, *args, **kwargs):
    data = {
        "id": post_id,
    }
    status = 200
    try:
        obj = Post.objects.get(id=post_id)
        data['content'] = obj.content,
        data['title'] = obj.title,
        data['slug'] = obj.slug,
        data['content'] = obj.content,
        data['upload_date'] = obj.upload_date,
        data['image_path'] = obj.image.url,
    except:
        data['message'] = f"Oops... I have not found {post_id}"
        status = 200

    return JsonResponse(data, status=status)

from django.http import Http404, JsonResponse
from django.shortcuts import render

from .models import Post
# Create your views here.


def post_detail_view(request, post_id, *args, **kwargs):
    try:
        obj = Post.objects.get(id=post_id)
    except:
        raise Http404
    data = {
        "id": post_id,
        "content": obj.content,
        # "image_path": obj.image.url,
    }
    return JsonResponse(data)
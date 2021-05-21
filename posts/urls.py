from django.urls import path

from .views import post_detail_view

urlpatterns = [
    path('<int:post_id>/', post_detail_view, name='post_detail'),

    # path('post')
]

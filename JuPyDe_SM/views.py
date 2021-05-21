from django.shortcuts import render
from django.http import JsonResponse


def home_page_view(request):
    template = 'JuPyDe_SM/index.html'
    context = {}

    return render(request, template, context)

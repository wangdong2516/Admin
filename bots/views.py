from django.shortcuts import render
from . import celery_tasks


def index(request):
    return render(request, 'bots/index.html', {})

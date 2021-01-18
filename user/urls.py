from django.urls import re_path
from user import views

urlpatterns = [
    re_path('test/$', views.IndexView.as_view()),
]

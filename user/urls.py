from django.urls import re_path
from user import views

urlpatterns = [
    re_path('login/$', views.LoginView.as_view(), name='login'),
    re_path('info/$', views.UserInfoVirew.as_view(), name='user_info'),
]

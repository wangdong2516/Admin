from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user import views

urlpatterns = [
    re_path('register/$', views.RegisterView.as_view(), name='register'),
    re_path('login/$', views.LoginView.as_view(), name='login'),
    re_path('info/$', views.UserInfoView.as_view(), name='user_info'),
    re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path('filter/', views.FilterView.as_view(), name='filter'),
    re_path('detail/(?P<pk>\d+)/$', views.FilterView.as_view(), name='detail'),
]

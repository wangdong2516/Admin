from django.shortcuts import render
from rest_framework.response import Response

from user.validation import IndexModel
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from user.serializers import UserSerializer

# Create your views here.
from utils.response import DRFResponse


class LoginView(APIView):
    """
        用户登录
    """
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(data=user_serializer.errors)
        return Response(data={"code": 20000, **user_serializer.data})


class UserInfoView(APIView):
    """
        用户信息
    """

    def get(self, request):
        d = {
            'roles': ['admin'],
            'introduction': 'I am a super administrator',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Super Admin'
        }
        return JsonResponse({'data': d, 'code': 20000})

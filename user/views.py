from datetime import datetime
from datetime import timedelta
from jwt import encode
from jwt import decode
from rest_framework.response import Response

from user.validation import IndexModel
from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from user.serializers import UserSerializer
from utils.error_code import UserErrorCode
# Create your views here.
from utils.response import DRFResponse


class RegisterView(APIView):
    """
        用户注册
    """

    def post(self, request):
        pass


class LoginView(APIView):
    """
        用户登录
    """
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(data=user_serializer.errors, status=400)

        token = request.headers.get('Authorization')
        if token:
            is_valid = decode(token, key=settings.JWT_TOKEN_SECRET_KEY)
            if not is_valid:
                return Response(data={'code': UserErrorCode.TOKEN_INVALID, 'message': '无效的token'})
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
        print(request.user)
        return JsonResponse({'data': d, 'code': 20000})

from rest_framework import serializers
from user.models import UserModel
from utils.error_code import UserErrorCode
from django.conf import settings
from jwt import encode


class UserSerializer(serializers.Serializer):
    """
        用户序列化器
    """
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=30, write_only=True)
    data = serializers.CharField(max_length=30, read_only=True)

    def validate_username(self, username: str):
        """
            单个字段的验证方法
        :param username: 验证的用户名
        :return:
        """
        try:
            UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError(
                {'error': '用户名不存在', 'code': UserErrorCode.NOTEXISTS}
            )
        return username

    def validate(self, validate_data):
        user = UserModel.objects.get(username=validate_data['username'])
        if not user.check_password(raw_password=validate_data['password']):
            raise serializers.ValidationError({'error': '密码错误', 'code': UserErrorCode.PASSERROR})

        # TODO:进行jwt_token签发
        payload = {
            'username': validate_data.pop('username')
        }

        token = encode(payload, key=settings.JWT_TOKEN_SECRET_KEY)

        validate_data['data'] = {
            'token': token
        }

        return validate_data

from rest_framework import serializers
from user.models import UserModel
from utils.error_code import ErrorCode


class UserSerializer(serializers.Serializer):
    """
        用户序列化器
    """
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=30, write_only=True)
    token = serializers.CharField(max_length=30, read_only=True)

    def validate_username(self, username: str):
        try:
            UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError({'error': '用户名不存在', 'code': ErrorCode.username_error})
        return username

    def validate(self, validate_data):
        user = UserModel.objects.get(username=validate_data['username'])
        if not user.check_password(raw_password=validate_data['password']):
            raise serializers.ValidationError({'error': '密码错误', 'code': ErrorCode.password_error})
        validate_data['token'] = validate_data.pop('username')
        return validate_data

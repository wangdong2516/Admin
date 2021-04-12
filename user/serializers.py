from datetime import datetime
from datetime import timedelta
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import UserModel, Manufacturer
from user.models import Product
from utils.error_code import UserErrorCode
from django.conf import settings
from jwt import encode


class UserRegisterSerializer(serializers.Serializer):
    """
        用户注册序列化器
    """
    username = serializers.CharField(max_length=20, min_length=5, write_only=True)
    password = serializers.CharField(max_length=20, min_length=5, write_only=True)
    re_password = serializers.CharField(max_length=20, min_length=5, write_only=True)
    is_remind = serializers.BooleanField(write_only=True)
    sms_code = serializers.CharField(max_length=6, write_only=True)

    def validate_sms_code(self):
        """
            验证短信验证码
        :return:
        """

        pass

    def validate(self):
        """
            多字段验证
        :return:
        """
        pass


class UserSerializer(serializers.Serializer):
    """
        用户序列化器
    """
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=30, write_only=True)
    data = serializers.DictField(read_only=True)

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

        # 进行jwt_token签发,默认过期时间为7天,注意这里使用simple_jwt的签发方式来进行jwt的签发
        refresh = RefreshToken.for_user(user)

        validate_data['data'] = {
            'token': str(refresh.access_token)
        }

        return validate_data


class ProductSerializer(serializers.ModelSerializer):

    # manufacturer = serializers.HyperlinkedRelatedField(view_name='detail', read_only=True)
    manufacturer = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'

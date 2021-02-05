from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserModel(AbstractUser):
    """
        用户模型
    """

    username = models.CharField('用户名', max_length=20, unique=True)
    last_login = models.DateTimeField('上次登录时间', auto_now=True)

    class Meta:
        db_table = 'user'


class WebsiteVisit(models.Model):
    """
        网站访问数
    """
    visit = models.BigIntegerField('访问数', null=False, default=0)
    create_time = models.DateField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'website_visit'

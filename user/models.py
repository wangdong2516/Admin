from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from utils.model import BaseModel


class UserModel(AbstractUser):
    """
        用户模型
    """

    username = models.CharField('用户名', max_length=20, unique=True)
    last_login = models.DateTimeField('上次登录时间', auto_now=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        # 自定义权限
        permissions = [
            ('export', 'Can export user'),
            ('view', 'Can view user')
        ]

    def __str__(self):
        return self.username


class WebsiteVisit(models.Model):
    """
        网站访问数
    """
    visit = models.BigIntegerField('访问数', null=False, default=0)
    create_time = models.DateField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'website_visit'


class SmbBlackList(models.Model):
    black_keyword = models.TextField(blank=True, null=True)
    level = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'smb_black_list'

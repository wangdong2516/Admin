from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.model import BaseModel

# Create your models here.


class UserModel(AbstractUser):
    """
        用户模型
    """

    username = models.CharField('用户名', max_length=20, unique=True)
    last_login = models.DateTimeField('上次登录时间', auto_now=True)

    class Meta:
        db_table = 'user'
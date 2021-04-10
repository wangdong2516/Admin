from utils.model import BaseModel
from django.db import models

from user.models import UserModel
# Create your models here.


class TaskList(BaseModel):
    """
        任务列表
    """
    task_name = models.CharField('任务名称', max_length=20, null=False, blank=False)
    task_status = models.IntegerField('任务执行情况,0:未知错误，1:执行成功，2:执行失败', default=0, null=False)
    task_result = models.JSONField('任务结果', default=dict)

    class Meta:
        db_table = 'task_list'
        verbose_name = '任务列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name


class Task(BaseModel):
    """
        任务
    """

    task = models.OneToOneField(TaskList, on_delete=models.CASCADE)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'
        verbose_name = '任务'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

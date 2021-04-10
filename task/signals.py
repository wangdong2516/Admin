import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from task.models import Task


signal_log = logging.getLogger('signal')


@receiver(signal=post_save, sender=Task, dispatch_uid='task_post_save_dispatcher')
def post_save_action(sender, instance=None, created=False, **kwargs):
    # 触发一个爬虫任务

    signal_log.info(
        f'task instance has been created, sender:{sender}, created:{created}， instance_id:{instance.id}')



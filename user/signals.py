import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.forms.models import model_to_dict

from user.models import UserModel


signal_log = logging.getLogger('signal')


# 注册信号
@receiver(signal=post_save, sender=UserModel, dispatch_uid='user_post_save_dispatcher')
def post_save_callback(sender, instance=None, created=False, **kwargs):
    """
        在User模型对象被保存之前执行的逻辑,必须在installed_apnps中显示注册
    :param sender: 信号发送者
    :param instance: 模型类实例
    :param created:
    :param kwargs:
    :return:
    """

    if isinstance(instance, UserModel):
        signal_log.info(f'user instance has been created, sender:{sender}, created:{created}， instance_id:{instance.id}')


# 注册信号
def post_delete_callback(sender, instance=None, using=None, **kwargs):
    """
        在User模型类实例被删除的时候接收信号并且处理
    :param sender: 信号发送者
    :param instance: 模型类实例
    :param using:
    :param kwargs:
    :return:
    """
    instance_obj = model_to_dict(instance)
    signal_log.info(f'user instance has been deleted, instance: {instance_obj}')


# dispatch_uid防止信号被重复注册
post_delete.connect(receiver=post_delete_callback, sender=UserModel, dispatch_uid='post_delete_dispatcher')

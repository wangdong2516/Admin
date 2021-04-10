from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'task'

    def ready(self):
        """
            注册信号
        :return:
        """
        from task.signals import post_save_action

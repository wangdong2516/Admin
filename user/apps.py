from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        """
            在app加载完成之后注册信号
        :return:
        """
        from user.signals import post_save_callback

"""
    自定义Django命令

    实现创建app的时候，自动创建urls.py文件
"""
from pathlib import Path
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    """
        自定义startapp命令，实现urls.py文件夹的自动创建
    """

    help = 'create urls.py when run python manage.py startapp <appname>'

    def handle(self, *args, **options):
        app_name = options.pop('name')
        print(app_name)
        target = options.pop('directory')
        # 禁止通过命令行参数的形式指定模板目录
        options.pop('template', None)
        # 拼接模板目录的路径
        template_dir = Path(__file__).parent.parent.parent / 'app_template'
        options['template'] = str(template_dir)
        super().handle('app', app_name, target, **options)

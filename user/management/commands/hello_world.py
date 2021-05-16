from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'say hello world'

    def add_arguments(self, parser):
        """
            添加参数选项
        :param parser: 命令行解析器
        :return:
        """
        parser.add_argument('other', nargs='+', type=str)

        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        """
            业务逻辑
        :param args:
        :param options:
        :return:
        """
        if options['delete']:
            self.stdout.write('delete')
        self.stdout.write('{}'.format(options))
        self.stdout.write('{}'.format(args))

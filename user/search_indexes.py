from haystack import indexes
from user.models import UserModel


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    """
        user模型索引类
        1. 有且仅有一个document=True的字段
        2. use_template指明了使用模型类中的那些字段来建立索引，需要建立模板文件
    """
    text = indexes.CharField(document=True, use_template=True)
    last_login = indexes.DateTimeField(model_attr='last_login')

    def get_model(self):
        """
            返回需要建立索引的模型
        :return:
        """
        return UserModel

    def index_queryset(self, using=None):
        """
            返回需要建立索引的数据集
        :param using:
        :return:
        """
        return self.get_model().objects.all()

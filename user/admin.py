from django.contrib import admin
from user.models import UserModel
from django.db.models import Q
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    """
        user admin 站点
    """

    # 指定在列表页面展示的内容
    list_display = ('id', 'username', 'first_name', 'last_name', 'last_login')

    # 指定可以在列表页面编辑的字段(方式一，直接指定)
    # list_editable = ('first_name', 'last_name')

    # 指定在列表页面可以进行查询的字段
    search_fields = ('username', 'id')

    # 分组展示字段,把谁括起来谁就是一个组的
    fieldsets = (
        ('第一组', {'fields': ('username', ('first_name', 'last_name'))}),
        ('第二组', {'fields': ('email', 'is_staff')})
    )

    def get_fieldsets(self, request, obj=None):
        """
            根据权限控制详情页字段的展示
        :param request:
        :param obj:
        :return:
        """
        group_names = self.get_group_names(request.user)
        return self.fieldsets

    def get_queryset(self, request):
        """
            数据集的权限控制
        :param request:
        :return:
        """
        queryset = super(UserAdmin, self).get_queryset(request)
        group_name = self.get_group_names(request.user)

        if not request.user.is_superuser:
            return queryset
        return queryset.filter(
            ~(Q(username='admin') | Q(username='wangdong'))
        )

    def get_list_editable(self, request):
        """
            根据组的不同，限制列表页面可以编辑的字段
        :param request:
        :return:
        """
        group_names = self.get_group_names(request.user)

        if request.user.is_superuser:
            return ('first_name', 'last_name')
        return ()

    def get_changelist_instance(self, request):
        """
            django框架默认调用的方法,通过该方法来获取列表页面可以修改的字段
        :param request:
        :return:
        """
        self.list_editable = self.get_list_editable(request)
        return super(UserAdmin, self).get_changelist_instance(request)

    def get_group_names(self, user):
        """
            获取用户所属的所有组
        :param user: 用户对象
        :return: group_names []
        """
        group_names = []

        for item in user.groups.all():
            group_names.append(item.name)

        return group_names


# 给admin站点注册模型以及管理模型
admin.site.register(UserModel, UserAdmin)

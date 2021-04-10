from django.contrib import admin

from task.models import Task
from task.models import TaskList
# Register your models here.


class TaskAdmin(admin.ModelAdmin):

    list_display = ('task', 'creator')


admin.site.register(Task, TaskAdmin)
# admin.site.register(TaskList, TaskAdmin)

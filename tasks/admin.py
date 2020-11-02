from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Task)
admin.site.register(TaskListModel)
admin.site.register(TaskListModel2)
admin.site.register(Task2)

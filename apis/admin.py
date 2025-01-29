from django.contrib import admin

from .models import Task, Label, TaskLabel


admin.site.register(Task)
admin.site.register(Label)
admin.site.register(TaskLabel)

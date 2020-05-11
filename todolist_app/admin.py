from django.contrib import admin
#from .models import TaskList
from todolist_app.models import TaskList

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','task', 'done', 'owner')

admin.site.register(TaskList, TaskListAdmin)

#admin.site.register(TaskList)

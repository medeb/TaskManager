from django.contrib import admin
from .models import TaskList,TeamList,TeamMembers
# Register your models here.

admin.site.register(TaskList)
admin.site.register(TeamList)
admin.site.register(TeamMembers)

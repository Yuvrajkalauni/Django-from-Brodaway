from django.contrib import admin
from todo.models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin (admin.ModelAdmin):
    list_display = ['user', 'title', 'discription', 'due_date', 'priority', 'completed', 'created_at']
    list_filter = ['completed', 'priority']
    search_fields = ['title']
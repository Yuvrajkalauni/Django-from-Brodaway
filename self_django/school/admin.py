from django.contrib import admin

from school.models import Teacher, Student

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name','dob','email','phone']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name','dob','email']
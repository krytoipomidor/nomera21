from django.contrib import admin

from core.models import Student
from core.models import Teacher
admin.site.register(Student)
admin.site.register(Teacher)

# Register your models here.

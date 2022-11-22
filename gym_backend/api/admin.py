from django.contrib import admin
from .models import Group, Student, Instructor, Room
# Register your models here.
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Room)

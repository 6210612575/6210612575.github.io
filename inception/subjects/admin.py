from django.contrib import admin

# Register your models here.

from .models import Subject


class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("studentInClass",)

admin.site.register(Subject, StudentAdmin)

#admin.site.register(Student)

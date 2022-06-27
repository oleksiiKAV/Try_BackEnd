# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-class-docstring
# pylint: disable=trailing-whitespace
from django.contrib import admin
from students.models import StudentGroup
from students.models import Student
from students.models import Subject

admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Subject)
# Register your models here.

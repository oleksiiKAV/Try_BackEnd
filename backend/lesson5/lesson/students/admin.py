# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from django.contrib import admin
from students.models import Student

admin.site.register(Student)
# Register your models here.

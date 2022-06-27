# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-class-docstring
# pylint: disable=trailing-whitespace
from django.contrib import admin
from django.urls import path
from students.views import ViewSubject, ViewAllStudents, ViewStudentUseID, ViewStudentsUseSubjectID

urlpatterns = [
    path('view1/', ViewAllStudents.as_view()), # /view1/ return all students in DB
    path('view2/<pk>/', ViewStudentUseID.as_view()), #/view2/2 - return stud with ID=2
    path('courses/subject/', ViewSubject.as_view()),
    path('courses/subject/<pk>', ViewStudentsUseSubjectID.as_view()),
]

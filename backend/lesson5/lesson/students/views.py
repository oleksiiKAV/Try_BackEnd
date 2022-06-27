# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=trailing-whitespace
# pylint: disable=E1101
from tokenize import group
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import StudentGroup
from students.models import Student
from students.models import Subject

def my_view(request):
    if request.method == 'get':
        return HttpResponse('result')

# return all students
class ViewAllStudents(View):
    def get(self, request):
        #id = 2
        students = Student.objects.all()
        students_data = []
        for student in students:
            students_data.append({
                "name":student.name
            })
        return JsonResponse({"data":students_data})
    def post(self, request):
        name = request.POST.get('name', '')
        print(name)
        return HttpResponse(name)

# return student with pk id  - /pk - id of student
class ViewStudentUseID(View):
    def get(self, request, pk):

        try:
            student = Student.objects.get(pk=pk)
            students_data = {
                "name":student.name
            }
        except Student.DoesNotExist:
            students_data = {}
        
        return JsonResponse({"data":students_data})

# return all subjects
class ViewSubject(View):
    def get(self, request):
        #id = 2
        name = request.GET.get('name', False)
        print(id)
        subjects = Subject.objects.all()
        if name:
            subjects = subjects.filter(name=name)

        subjects_data = []
        for subject in subjects:
            subjects_data.append({
                "name":subject.name
            })
        return JsonResponse({"data":subjects_data})

    def post(self, request):
        name = request.POST.get('name', '')
        print(name)
        return HttpResponse(name)

# return students with subject id - /pk - id of student
class ViewStudentsUseSubjectID(View):
    #from django.db.models import query
    def get(self, request, pk):

        try:
            # по group из Групп и по subjects из преметов, который равен id
            students=Student.objects.filter(group__subjects__id=pk)
            students_data = []
            
            for student in students:
                students_data.append({
                  "name":student.name,
                })
        
        except Subject.DoesNotExist:
            students_data = {}
        
        return JsonResponse({"data":students_data})
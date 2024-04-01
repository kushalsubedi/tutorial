from django.shortcuts import render
from django.http import HttpResponse

from .models import Student


def index (request):

    """
    SELECT * FROM Student
    """
    students = Student.objects.all()
    context = {
        'students':students
    }


    return  render(request,'Home/index.html',context)


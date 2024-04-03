from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from .forms import StudentCreationForm, UpdateStudentForm

def index (request):

    """
    SELECT * FROM Student
    """
    students = Student.objects.all()
    context = {
        'students':students
    }


    return  render(request,'Home/index.html',context)


def retrive_student(request,id):
    student = Student.objects.get(pk=id)
    context = {
        'student':student
    }
    return render (request,'Home/retrive.html',context)

# def add_student (request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         roll = request.POST.get('roll')
#         city = request.POST.get('city')
#         student = Student(name=name,roll=roll,city=city)
#         student.save()
#         return HttpResponse("Student Added Successfully")
#     else :
#         return render(request,'Home/add_student.html')
    
def add_student (request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Student Added Successfully")
    return render(request,'Home/add_student.html',{'form':form})

    
# def update_student(request,id):
#     student = Student.objects.get(pk=id)

#     """
#         select * from Student where id = %id
#     """


#     if request.method == 'POST':
#         name = request.POST.get('name')
#         roll = request.POST.get('roll')
#         city = request.POST.get('city')
#         student.name = name
#         student.roll = roll
#         student.city = city
#         student.save()
#         return HttpResponse("Student Updated Successfully")
#     else :
#         return render(request,'Home/add_student.html',{'student':student})


def update_student(request,id):
    student = Student.objects.get(pk=id)
    form = UpdateStudentForm(instance=student)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse("Student Updated Successfully")
    return render(request,'Home/update.html',{'form':form})
    
def delete_student(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return HttpResponse("Student Deleted Successfully")


# create new project that consist of groceries items and perform crud operation on it 
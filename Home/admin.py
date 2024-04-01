from django.contrib import admin

# Register your models here.


from .models import Student , Exam_Result

admin.site.register(Student)

admin.site.register(Exam_Result)
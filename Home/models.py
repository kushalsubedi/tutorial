from django.db import models

# Create your models here.

class Student (models.Model):
    # id = primary key
    name = models.CharField(max_length=100)
    roll = models.IntegerField(null=True, blank=True) 
    city = models.CharField(max_length=100)
   
    """
    CREATE TABLE Student name varchar(100),roll int,city varchar(100)
  
    """
    def __str__(self):
        return self.name

class Exam_Result (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # relationship with student table 


    """
    naya field (student)   --> (Student table) 
    """
   
    percentage = models.FloatField()
    grade = models.CharField(max_length=10)
  
    def __str__(self):
        return self.student.name

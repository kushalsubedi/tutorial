from django.db import models

# Create your models here.

class Student (models.Model):
    # id = primary key
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
   
    """
    CREATE TABLE Student name varchar(100),roll int,city varchar(100)
  
    """
    def __str__(self):
        return self.name

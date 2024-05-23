from django.db import models

# Create your models here.
class Course(models.Model):
    CourseName = models.CharField(max_length=25)

    def __str__(self):
        return self.CourseName

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
    phoneNo = models.BigIntegerField(default=0)
    Email = models.CharField(max_length=30)
    Age = models.IntegerField()


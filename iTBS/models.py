from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    student_nb = models.CharField(max_length=10, unique=True)

    def __student__(self):
        return f"{student.first_name} {student.last_name} ({student.student_nb})"

# Create your models here.

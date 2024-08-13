from django.apps import AppConfig

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_number})"


class ItbsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iTBS'

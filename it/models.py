from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    regenumber = models.IntegerField()
    age = models.IntegerField()
    department = models.CharField(max_length=20)
    def _str__(self):
        return self.name

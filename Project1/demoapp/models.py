from django.db import models
from django.forms import ModelForm

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    image=models.FileField(upload_to="media/",default="")

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields=["name","email","password","contact","image"]
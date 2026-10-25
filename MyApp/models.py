from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    place=models.CharField(max_length=100,null=True)
    contact=models.IntegerField(null=True)
    email=models.EmailField(max_length=100,null=True)
    qualification=models.CharField(max_length=100,null=True)
    experience=models.IntegerField(null=True)
    subject=models.CharField(max_length=100,null=True)
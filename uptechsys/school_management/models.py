from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    dob = models.DateTimeField()
    address = models.CharField(max_length=150)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_phone_number = models.IntegerField()
    mother_phone_number = models.IntegerField()
    father_occupation = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)


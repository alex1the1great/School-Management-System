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

    def __init__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    school_type = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    established = models.DateField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    school = models.ManyToManyField(School)
    salary = models.FloatField()

    def __init__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    subject_teacher = models.ManyToManyField(Teacher)
    subject_faculty = models.ManyToManyField(Faculty)

    def __init__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=200)
    exam_date = models.DateTimeField()
    student_exam = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __init__(self):
        return self.name

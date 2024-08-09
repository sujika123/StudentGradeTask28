from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)


class teacherlogin(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='teacher',null=True)
    name=models.CharField(max_length=50)
    teacher_id=models.CharField(max_length=40)
    course=models.CharField(max_length=50)




class studentlogin(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='student',null=True)
    name=models.CharField(max_length=50)
    student_id = models.CharField(max_length=40)
    course = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)

    def __str__(self):
         return self.name



class courseadd(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=60)
    course_id = models.CharField(max_length=40)

    def __str__(self):
         return self.title


class gradeadd(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(studentlogin, on_delete=models.CASCADE, null=True, blank=True, related_name='Student')
    course = models.ForeignKey(courseadd, on_delete=models.CASCADE, null=True, blank=True, related_name='Course')
    year = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)




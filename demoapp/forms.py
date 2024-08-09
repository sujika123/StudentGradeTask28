from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, teacherlogin, studentlogin, courseadd, gradeadd


class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2= forms.CharField(widget=forms.PasswordInput, label='confirm password')
    class Meta:
        model=Login
        fields=('username','password1','password2',)


class teacherloginform(forms.ModelForm):

    class Meta:
        model=teacherlogin
        fields=('name','teacher_id','course')


class studentloginform(forms.ModelForm):

    class Meta:
        model=studentlogin
        fields=('name','student_id','course','semester',)


class courseddform(forms.ModelForm):

    class Meta:
        model=courseadd
        fields=('title','course_id')


class gradeform(forms.ModelForm):

    class Meta:
        model=gradeadd
        fields=('student','course','year','semester','grade')


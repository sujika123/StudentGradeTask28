from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from demoapp.forms import LoginForm, teacherloginform, studentloginform, courseddform, gradeform
from demoapp.models import studentlogin, courseadd, gradeadd


# Create your views here.
def home(request):
    return render(request,'home.html')


def teacher_registeration(request):
    form = LoginForm()
    form1 = teacherloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = teacherloginform(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = form1.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect(loginview)
    return render(request, 'teacher_registration.html', {'form': form, 'form1': form1})


def student_registeration(request):
    form = LoginForm()
    form1 = studentloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = studentloginform(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            teacher = form1.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect(loginview)
    return render(request, 'student_registration.html', {'form': form, 'form1': form1})



def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
             login(request, user)
             return redirect('adminhome')

        if user is not None and user.is_teacher:
            login(request, user)
            return redirect('teacher')

        if user is not None and user.is_student:
            login(request, user)
            return redirect('student')
        else:
            messages.info(request, 'Invalid Credentials')

    return render(request, 'login.html')


def student(request):
    return render(request,'student/studenthome.html')

def teacher(request):
    return render(request,'teacher/teacherhome.html')

def stdprofileview(request):
    u = request.user
    data = studentlogin.objects.filter(user=u)
    print(data)
    return render(request, 'student/student_profileview.html', {'data': data})

def tview_students(request):
    data = studentlogin.objects.all()
    print(data)
    return render(request,'teacher/view_students.html', {'data':data})


def studentupdate(request,id):
    user=studentlogin.objects.get(id=id)
    form=studentloginform(instance=user)
    if request.method == "POST":
        form= studentloginform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('tview_students')
    return render(request,'teacher/update_student.html',{'form':form})

def studentdelete(request,id):
    data=studentlogin.objects.get(id=id)
    data.delete()
    return redirect('tview_students')


# Course

def addcourse(request):
    form = courseddform()
    u = request.user
    if request.method=='POST':
        form = courseddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewcourses')
    return render(request,'teacher/add_course.html',{'form':form})


def viewcourses(request):
    data = courseadd.objects.all()
    return render(request,'teacher/view_course.html',{'data':data})


def courseupdate(request,id):
    data = courseadd.objects.get(id=id)
    form = courseddform(instance=data)
    if request.method == "POST":
        form = courseddform(request.POST or None, request.FILES, instance=data or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('viewcourses')
    return render(request, 'teacher/update_course.html', {'form': form})


def coursedelete(request,id):
    data = courseadd.objects.get(id=id)
    data.delete()
    return redirect('viewcourses')


# Grade

def addgrade(request):
    form = gradeform()
    u = request.user
    if request.method=='POST':
        form = gradeform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('view_grade')
    return render(request,'teacher/add_grade.html',{'form':form})


def view_grade(request):
    data = gradeadd.objects.all()
    return render(request,'teacher/view_grade.html',{'data':data})


def gradeupdate(request,id):
    data = gradeadd.objects.get(id=id)
    form = gradeform(instance=data)
    if request.method == "POST":
        form = gradeform(request.POST or None, request.FILES, instance=data or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('view_grade')
    return render(request, 'teacher/update_grade.html', {'form': form})


def gradedelete(request,id):
    data = gradeadd.objects.get(id=id)
    data.delete()
    return redirect('view_grade')


def stdview_grade(request):
    u = request.user
    user = studentlogin.objects.get(user=u)
    data = gradeadd.objects.filter(student=user)
    return render(request,'student/view_grade.html',{'data':data})

def calculate_GPA(request):
    grades = {
        'A': 4.0,
        'A-': 3.66,
        'B+': 3.33,
        'B': 3.0,
        'B-': 2.66,
        'C+': 2.33,
        'C': 2.0,
        'C-': 1.66,
        'D+': 1.33,
        'D': 1.00,
        'D-': .66,
        'F': 0.00
    }

    if grade in grades:
        return grades.get(grade.upper())
    else:
        return "Invalid"


    grades = [GPAcalc(grade) for grade in ("A", "B", "C", "D")]
    print(grades)
    total = 0
    for grade in grades:

        if grade != "Invalid":
           total += grade
    print(total)
    gpa = total / len(grades)
    print(gpa)
from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('teacher_registeration',views.teacher_registeration,name='teacher_registeration'),
    path('student_registeration',views.student_registeration,name='student_registeration'),
    path('loginview',views.loginview,name='loginview'),
    path('student',views.student,name='student'),
    path('teacher',views.teacher,name='teacher'),
    path('stdprofileview',views.stdprofileview,name='stdprofileview'),
    path('tview_students',views.tview_students,name='tview_students'),
    path('studentupdate/<int:id>/',views.studentupdate,name='studentupdate'),
    path('studentdelete/<int:id>/',views.studentdelete,name='studentdelete'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('viewcourses',views.viewcourses,name='viewcourses'),
    path('courseupdate/<int:id>/',views.courseupdate,name='courseupdate'),
    path('coursedelete/<int:id>/',views.coursedelete,name='coursedelete'),
    path('addgrade',views.addgrade,name='addgrade'),
    path('view_grade',views.view_grade,name='view_grade'),
    path('gradeupdate/<int:id>/', views.gradeupdate, name='gradeupdate'),
    path('gradedelete/<int:id>/', views.gradedelete, name='gradedelete'),
    path('stdview_grade',views.stdview_grade,name='stdview_grade'),


]
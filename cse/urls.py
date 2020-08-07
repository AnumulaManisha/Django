from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('achieve/', views.achieve, name='achieve'),
    path('contact/', views.contact, name='contact'),
    path('placement/', views.placement, name='placement'),
    path('faculty/', views.faculty, name='faculty'),
    path('Studentlogin/', views.Studlogin, name='Studlogin'),
    path('Studentlogin/Studentsignup/', views.Studsignup, name='Studsignup'),
    path('Studentlogin/Studentportal/', views.Studentportal, name='Studentportal'),
    path('Studentlogin/Studentportal/logout/', views.logout, name='logout'),
    path('Studentlogin/Studentportal/Attendance/', views.Attendance, name='Attendance'),
    path('Studentlogin/Studentportal/Timetable/', views.Timetable, name='Timetable'),
    path('Studentlogin/Studentportal/FeedbackForm/', views.FeedbackForm, name='FeedbackForm'),
    path('Studentlogin/Studentportal/UploadDisplay/', views.UploadDisplay, name='UploadDisplay'),
    path('Teacherlogin/', views.Teacherlogin, name='Teacherlogin'),
    path('Teacherlogin/Teachersignup/', views.Teachersignup, name='Teachersignup'),
    path('Teacherlogin/Teacherportal/', views.Teacherportal, name='Teacherportal'),
    path('Teacherlogin/Teacherportal/Teacherlogout/', views.Teacherlogout, name='Teacherlogout'),
    path('Teacherlogin/Teacherportal/upload/', views.upload, name='upload'),
]
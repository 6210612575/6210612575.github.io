from django.contrib import admin
from django.urls import path
from . import views


app_name="subjects"

urlpatterns =[
    path('',views.index , name="index"),
    path('<int:subject_id>',views.subject,name="subject"),
    path('<str:subject_id>/enroll' ,views.enroll,name="enroll"),
    path('<str:subject_id>/drop' ,views.drop,name="drop"),
    path('Course' ,views.Course,name="Course"),

    ]
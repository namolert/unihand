from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.student_home, name="student_home"),
]

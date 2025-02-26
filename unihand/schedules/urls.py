from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_schedules_view, name="course_schedules"),
]
from django.urls import path
from . import views
from enrollments.views import enrolled_students_view

urlpatterns = [
    path("", views.professor_home, name="professor_home"),
    path("course-schedule/", views.professor_course_schedule, name="professor_course_schedule"),
    path("view-grades/", views.view_grades_view, name="view_grades_view"),
    path('enrolled-students/', enrolled_students_view, name='enrolled_students'),
]

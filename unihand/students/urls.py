from django.urls import path
from . import views
from enrollments.views import enrolled_classes_view
from grades.views import my_grades_view
from schedules.views import student_course_schedule

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("course-schedule/", student_course_schedule, name="student_course_schedule"),
    path("my-grades/", my_grades_view, name="my_grades"),
    path('enrolled-classes/', enrolled_classes_view, name='enrolled_classes'),
]

from django.urls import path
from . import views
from enrollments.views import enrolled_classes_view

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("course-schedule/", views.student_course_schedule, name="student_course_schedule"),
    path("my-grades/", views.my_grades_view, name="my_grades"),
    path('enrolled-classes/', enrolled_classes_view, name='enrolled_classes'),
]

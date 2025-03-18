from django.urls import path
from . import views
from enrollments.views import enrolled_students_view, enrolling_view
from grades.views import view_grades_view
from schedules.views import professor_course_schedule

urlpatterns = [
    path("", views.professor_home, name="professor_home"),
    path("course-schedule/", professor_course_schedule, name="professor_course_schedule"),
    path("view-grades/", view_grades_view, name="view_grades_view"),
    path('enrolled-students/', enrolled_students_view, name='enrolled_students'),
    path("enrolling/<int:course_id>/", enrolling_view, name="enrolling"),
]

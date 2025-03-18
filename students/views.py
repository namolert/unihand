from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from enrollments.models import Enrollment
from schedules.models import CourseSchedule
from appointments.models import Appointment
from todos.models import ToDo
from grades.models import Grade

@login_required
def student_home(request):
    student = request.user.student
    enrolled_courses = Enrollment.objects.filter(student=request.user.student).values_list("course", flat=True)
    student_schedule = CourseSchedule.objects.filter(course_id__in=enrolled_courses)
    appointments = Appointment.objects.filter(student=request.user.student)
    todos = ToDo.objects.filter(student=request.user.student)

    context = {
        "course_schedule": student_schedule,
        "student": student,
        "enrolled_courses": enrolled_courses,
        "appointments": appointments,
        "todos": todos,
    }
    return render(request, "main/home.html", context)

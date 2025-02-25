from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from enrollments.models import Enrollment
from schedules.models import CourseSchedule
from appointments.models import Appointment
from todos.models import ToDo

@login_required
def student_home(request):
    student = request.user.student
    course_schedule = CourseSchedule.objects
    enrollments = Enrollment.objects.filter(student=request.user.student)
    appointments = Appointment.objects.filter(student=request.user.student)
    todos = ToDo.objects.filter(student=request.user.student)

    context = {
        "course_schedule": course_schedule,
        "student": student,
        "enrollments": enrollments,
        "appointments": appointments,
        "todos": todos,
    }
    return render(request, "students/home.html", context)

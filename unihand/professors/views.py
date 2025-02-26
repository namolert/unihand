from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Professor
from courses.models import Course
from enrollments.models import Enrollment
from schedules.models import CourseSchedule
from appointments.models import Appointment
from grades.models import Grade

@login_required
def professor_home(request):
    professor = request.user.professor
    courses_taught = professor.courses_taught.all()  
    professor_schedule = CourseSchedule.objects.filter(course__in=courses_taught)
    enrollments = Enrollment.objects.filter(course__in=courses_taught)
    appointments = Appointment.objects.filter(professor=professor)

    context = {
        "professor": professor,
        "course_schedule": professor_schedule,
        "enrollments": enrollments,
        "appointments": appointments,
    }
    return render(request, "professors/home.html", context)

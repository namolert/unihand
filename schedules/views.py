from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment
from schedules.models import CourseSchedule

@login_required
def student_course_schedule(request):
    student = request.user.student  
    course_schedule = CourseSchedule.objects.filter(course__enrollments__student=student)

    # List of days of the week
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    context = {
        "course_schedule": course_schedule,
        "days_of_week": days_of_week,
    }
    return render(request, "schedules/students/course_schedule.html", context)

@login_required
def professor_course_schedule(request):
    professor = request.user.professor
    course_schedule = CourseSchedule.objects.filter(professor=professor)

    context = {
        "course_schedule": course_schedule,
    }
    return render(request, "schedules/professors/course_schedule.html", context)
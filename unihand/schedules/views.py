from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment
from schedules.models import CourseSchedule

@login_required
def student_course_schedule(request):
    student = request.user.student
    enrolled_courses = Enrollment.objects.filter(student=student).values_list("course", flat=True)
    course_schedule = CourseSchedule.objects.filter(course_id__in=enrolled_courses)

    context = {
        "course_schedule": course_schedule,
    }
    return render(request, "schedules/students/course_schedule.html", context)

@login_required
def professor_course_schedule(request):
    professor = request.user.professor
    courses_taught = CourseSchedule.objects.filter(professor=professor)

    context = {
        "course_schedule": courses_taught,
    }
    return render(request, "schedules/professors/course_schedule.html", context)

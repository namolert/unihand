from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course, Grade

@login_required
def my_grades_view(request):
    student = request.user.student
    grades = Grade.objects.filter(student=student)
    
    context = {
        "grades": grades
    }
    return render(request, "grades/students/my_grades.html", context)

@login_required
def view_grades_view(request):
    professor = request.user.professor
    courses_taught = Course.objects.filter(professors=professor)
    grades = Grade.objects.filter(course__in=courses_taught)
    
    context = {
        "grades": grades
    }
    return render(request, "grades/professors/view_grades.html", context)

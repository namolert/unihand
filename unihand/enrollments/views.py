from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def enrolled_classes_view(request):
    return render(request, "enrollments/students/enrolled_classes.html")

@login_required
def enrolled_students_view(request):
    return render(request, "enrollments/professors/enrolled_students.html")
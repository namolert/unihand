from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from enrollments.models import Enrollment
from .forms import EnrollmentForm
from django.core.exceptions import ObjectDoesNotExist

@login_required
def enrolled_classes_view(request):
    try:
        student = request.user.student
    except ObjectDoesNotExist:
        messages.error(request, "You are not associated with any student profile.")
        return redirect('some_error_page')

    enrolled_courses = Course.objects.filter(enrollments__student=student)

    context = {
        "enrolled_courses": enrolled_courses
    }
    return render(request, "enrollments/students/enrolled_classes.html", context)

@login_required
def enrolled_students_view(request):
    try:
        professor = request.user.professor
    except ObjectDoesNotExist:
        messages.error(request, "You are not associated with any professor profile.")
        return redirect('some_error_page')

    courses_taught = professor.courses_taught.all()

    context = {
        "courses_taught": courses_taught
    }
    return render(request, "enrollments/professors/enrolled_students.html", context)

@login_required
def enrolling_view(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    professor = request.user.professor

    if course not in professor.courses_taught.all():
        messages.error(request, "You are not assigned to this course.")
        return redirect("enrolled_students")

    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data["student"]
            enrollment, created = Enrollment.objects.get_or_create(course=course, student=student)
            if created:
                messages.success(request, f"{student.user.get_full_name()} enrolled successfully!")
            else:
                messages.warning(request, "Student is already enrolled in this course.")
            return redirect("enrolled_students")
    else:
        form = EnrollmentForm()

    return render(request, "enrollments/professors/enrolling.html", {"form": form, "course": course})

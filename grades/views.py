from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from enrollments.models import Enrollment
from grades.models import Grade

@login_required
def my_grades_view(request):
    student = request.user.student
    enrollments = Enrollment.objects.filter(student=student).select_related("course")
    grades = {grade.course_id: grade for grade in Grade.objects.filter(student=student)}

    courses_with_grades = []
    for enrollment in enrollments:
        course = enrollment.course
        course_grade = grades.get(course.course_id, None)
        courses_with_grades.append({
            "course": course,
            "grade": course_grade.grade if course_grade else "Not Graded",
            "comments": course_grade.comments if course_grade else "",
        })

    context = {
        "courses_with_grades": courses_with_grades
    }
    return render(request, "grades/students/my_grades.html", context)

@login_required
def view_grades_view(request):
    professor = request.user.professor
    courses_taught = Course.objects.filter(professors=professor)

    selected_course_id = request.GET.get("course_id")
    students_with_grades = []

    if selected_course_id:
        selected_course = get_object_or_404(Course, course_id=selected_course_id, professors=professor)
        enrollments = Enrollment.objects.filter(course=selected_course).select_related("student__user")
        grades = {grade.student.student_id: grade for grade in Grade.objects.filter(course=selected_course)}

        for enrollment in enrollments:
            student = enrollment.student
            student_grade = grades.get(student.student_id, None)
            students_with_grades.append({
                "student": student,
                "grade": student_grade.grade if student_grade else "Not Graded",
                "comments": student_grade.comments if student_grade else "",
            })
    else:
        selected_course = None

    context = {
        "courses_taught": courses_taught,
        "selected_course": selected_course,
        "students_with_grades": students_with_grades,
    }
    return render(request, "grades/professors/view_grades.html", context)

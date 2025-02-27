import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unihand.settings")
django.setup()

from users.models import User
from students.models import Student
from professors.models import Professor
from programs.models import Program
from courses.models import Course
from enrollments.models import Enrollment
from grades.models import Grade
from schedules.models import CourseSchedule
from mock_data import mock_users, mock_programs, mock_courses, mock_enrollments, mock_grades, mock_schedules

# Delete users
for user_data in mock_users:
    user = User.objects.filter(username=user_data["username"]).first()
    if user:
        if user_data["role"] == "Student":
            Student.objects.filter(user=user).delete()
        elif user_data["role"] == "Professor":
            Professor.objects.filter(user=user).delete()
        user.delete()
        print(f"Deleted user: {user.username}")

# Delete programs
for program_data in mock_programs:
    Program.objects.filter(program_code=program_data["program_code"]).delete()
    print(f"Deleted program: {program_data['program_code']}")

print("Mock data deletion complete!")

# Delete enrollments
for enrollment_data in mock_enrollments:
    student = User.objects.filter(username=enrollment_data["student_username"]).first()
    course = Course.objects.filter(course_code=enrollment_data["course_code"]).first()
    if student and course:
        Enrollment.objects.filter(student=student.student, course=course).delete()
        print(f"Deleted enrollment: {student.username} -> {course.course_code}")

# Delete grades
for grade_data in mock_grades:
    student = User.objects.filter(username=grade_data["student_username"]).first()
    course = Course.objects.filter(course_code=grade_data["course_code"]).first()
    if student and course:
        Grade.objects.filter(student=student.student, course=course).delete()
        print(f"Deleted grade: {student.username} -> {course.course_code}")

# Delete course schedules
for schedule_data in mock_schedules:
    course = Course.objects.filter(course_code=schedule_data["course_code"]).first()
    professor = Professor.objects.filter(user__username=schedule_data["professor_username"]).first()
    if course and professor:
        CourseSchedule.objects.filter(course=course, professor=professor).delete()
        print(f"Deleted schedule for course: {course.course_code}")

# Delete courses
for course_data in mock_courses:
    Course.objects.filter(course_code=course_data["course_code"]).delete()
    print(f"Deleted course: {course_data['course_code']}")


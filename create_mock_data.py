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

# Mock Programs
for program_data in mock_programs:
    program, created = Program.objects.get_or_create(
        program_code=program_data["program_code"],
        defaults={"program_name": program_data["program_name"]}
    )
    if created:
        print(f"Program created: {program.program_name}")
    else:
        print(f"Program {program.program_name} already exists.")

# Mock Users
for user_data in mock_users:
    user, created = User.objects.get_or_create(
        username=user_data["username"],
        defaults={
            "email": user_data["email"],
            "role": user_data["role"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"]
        }
    )

    if created:
        user.set_password(user_data["password"])
        user.save()
        print(f"Mock user created: {user.username} ({user.role})")
    else:
        print(f"User {user.username} already exists.")

    if user_data["role"] == "Student":
        # Select CS101 program for this mock user
        program_code = Program.objects.filter(program_code="CS101").first()

        student, student_created = Student.objects.get_or_create(
            user=user,
            defaults={
                "student_id": f"{user.id}{user.last_name[0].upper() if user.last_name else 'X'}",
                "program_code": program_code,
                "gpa": 3.5,
                "status": "ResultAwaiting"
            }
        )
        if student_created:
            print(f"Student record created for {user.first_name} {user.last_name}")

    elif user_data["role"] == "Professor":
        professor, prof_created = Professor.objects.get_or_create(
            user=user,
            defaults={
                "professor_id": f"P{user.id}",
                "department": "Computer Science"
            }
        )
        if prof_created:
            print(f"Professor record created for {user.first_name} {user.last_name}")

# Mock Courses
for course_data in mock_courses:
    program = Program.objects.filter(program_code=course_data["program_code"]).first()
    if program:
        course, created = Course.objects.get_or_create(
            course_code=course_data["course_code"],
            defaults={
                "course_name": course_data["course_name"],
                "program_code": program,
                "semester_number": course_data["semester_number"],
                "course_type": course_data["course_type"],
                "credits": course_data["credits"],
                "academic_year_added": course_data["academic_year_added"],
            }
        )
        if created:
            print(f"Course created: {course.course_name}")
        else:
            print(f"Course {course.course_name} already exists.")

# Assign Professor to the Course
professor = Professor.objects.filter(user__username="mockprofessor").first()
if professor:
    course_codes = ["CS201", "CS202"]
    
    for course_code in course_codes:
        course = Course.objects.filter(course_code=course_code).first()
        if course:
            course.professors.add(professor)
            print(f"Assigned {professor.user.first_name} {professor.user.last_name} to {course.course_name}")
        else:
            print(f"Course {course_code} not found.")
else:
    print("Mock professor not found.")

# Mock Enrollments
for enrollment_data in mock_enrollments:
    student = User.objects.filter(username=enrollment_data["student_username"]).first()
    course = Course.objects.filter(course_code=enrollment_data["course_code"]).first()
    
    if student and course:
        enrollment, created = Enrollment.objects.get_or_create(
            student=student.student,
            course=course,
            defaults={"created_by": enrollment_data["created_by"]}
        )
        if created:
            print(f"Enrollment created: {student.username} -> {course.course_name}")
        else:
            print(f"Enrollment already exists: {student.username} -> {course.course_name}")

# Mock Grades
for grade_data in mock_grades:
    student = User.objects.filter(username=grade_data["student_username"]).first()
    professor = User.objects.filter(username=grade_data["professor_username"], role="Professor").first()
    course = Course.objects.filter(course_code=grade_data["course_code"]).first()
    
    if student and professor and course:
        grade, created = Grade.objects.get_or_create(
            student=student.student,
            course=course,
            professor=professor,
            defaults={"grade": grade_data["grade"], "comments": grade_data["comments"]}
        )
        if created:
            print(f"Grade recorded: {student.username} -> {course.course_name}: {grade.grade}")
        else:
            print(f"Grade already exists for {student.username} in {course.course_name}")

# Mock Course Schedules
for schedule_data in mock_schedules:
    course = Course.objects.filter(course_code=schedule_data["course_code"]).first()
    professor = Professor.objects.filter(user__username=schedule_data["professor_username"]).first()
    
    if course and professor:
        schedule, created = CourseSchedule.objects.get_or_create(
            academic_year=schedule_data["academic_year"],
            course=course,
            professor=professor,
            defaults={
                "is_scheduled": schedule_data["is_scheduled"],
                "is_online": schedule_data["is_online"],
                "schedule_start": schedule_data["schedule_start"],
                "schedule_end": schedule_data["schedule_end"],
                "course_type": schedule_data["course_type"],
                "created_by": schedule_data["created_by"],
                "recurrence_rule": schedule_data["recurrence_rule"],
            }
        )
        if created:
            print(f"Schedule created for {course.course_name} in {schedule.academic_year}")
        else:
            print(f"Schedule already exists for {course.course_name} in {schedule.academic_year}")

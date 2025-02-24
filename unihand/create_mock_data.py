import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unihand.settings")
django.setup()

from users.models import User
from students.models import Student
from professors.models import Professor
from programs.models import Program
from mock_data import mock_users, mock_programs

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
        program = Program.objects.filter(program_code="CS101").first()

        student, student_created = Student.objects.get_or_create(
            user=user,
            defaults={
                "student_id": f"{user.id}{user.last_name[0].upper() if user.last_name else 'X'}",
                "program_code": program,
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

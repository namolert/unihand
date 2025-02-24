import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unihand.settings")
django.setup()

from users.models import User
from students.models import Student
from professors.models import Professor
from programs.models import Program
from mock_data import mock_users, mock_programs

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

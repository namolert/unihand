from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from students.models import Student
from programs.models import Program

class StudentModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            first_name="John",
            last_name="Doe",
            email="testuser@example.com",
            password="password123"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(
            user=self.user,
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )

    def test_student_creation(self):
        student = Student.objects.get(student_id="S12345")
        self.assertEqual(student.user.first_name, "John")
        self.assertEqual(student.program_code, self.program)
        self.assertEqual(student.gpa, 3.5)
        self.assertEqual(student.status, "ResultAwaiting")

    def test_student_str_method(self):
        self.assertEqual(str(self.student), "John Doe (S12345)")


class StudentViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(
            user=self.user,
            student_id="S12345",
            program_code=self.program
        )

    def test_student_home_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("student_home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")
        self.assertContains(response, "S12345")

    def test_student_home_unauthenticated(self):
        response = self.client.get(reverse("student_home"))
        self.assertEqual(response.status_code, 302)  # Redirect to login page
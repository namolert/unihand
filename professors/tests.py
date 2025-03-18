from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from professors.models import Professor

class ProfessorModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="professoruser",
            first_name="Alice",
            last_name="Smith",
            email="professor@example.com",
            password="password123"
        )
        self.professor = Professor.objects.create(
            user=self.user,
            professor_id="P12345",
            department="Computer Science"
        )

    def test_professor_creation(self):
        professor = Professor.objects.get(professor_id="P12345")
        self.assertEqual(professor.user.first_name, "Alice")
        self.assertEqual(professor.department, "Computer Science")

    def test_professor_str_method(self):
        self.assertEqual(str(self.professor), "Alice Smith (P12345)")


class ProfessorViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123"
        )
        self.professor = Professor.objects.create(
            user=self.user,
            professor_id="P12345",
            department="Computer Science"
        )

    def test_professor_home_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("professor_home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")
        self.assertContains(response, "P12345")

    def test_professor_home_unauthenticated(self):
        response = self.client.get(reverse("professor_home"))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

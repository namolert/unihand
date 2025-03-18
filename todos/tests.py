from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime, timedelta
from students.models import Student
from programs.models import Program
from todos.models import ToDo
import pytz

User = get_user_model()

class ToDoModelTest(TestCase):

    def setUp(self):
        self.student_user = User.objects.create_user(
            username="student1",
            password="password123",
            first_name="John",
            last_name="Doe",
            email="student@example.com"
        )

        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(user=self.student_user, student_id="S12345", program_code=self.program, gpa=3.8, status="Active")

        self.todo = ToDo.objects.create(
            student=self.student,
            task_description="Complete assignment",
            deadline=datetime.now(pytz.UTC) + timedelta(days=3),
            status="Not Start"
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.student, self.student)
        self.assertEqual(self.todo.task_description, "Complete assignment")
        self.assertEqual(self.todo.status, "Not Start")

    def test_todo_str_representation(self):
        expected_str = "Complete assignment (Not Start)"
        self.assertEqual(str(self.todo), expected_str)


class ToDoViewTest(TestCase):

    def setUp(self):
        self.student_user = User.objects.create_user(username="student1", password="password123")

        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(user=self.student_user, student_id="S12345", program_code=self.program, gpa=3.8, status="Active")

        self.todo = ToDo.objects.create(
            student=self.student,
            task_description="Complete project",
            deadline=datetime.now(pytz.UTC) + timedelta(days=2),
            status="In Progress"
        )

    def test_todos_view_authenticated(self):
        self.client.login(username="student1", password="password123")
        response = self.client.get(reverse("todos"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Complete project")

    def test_create_todo_view(self):
        self.client.login(username="student1", password="password123")
        response = self.client.post(reverse("todos"), {
            "task_description": "Prepare for exams",
            "deadline": (datetime.now(pytz.UTC) + timedelta(days=5)).strftime("%Y-%m-%dT%H:%M"),
            "status": "Not Start"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(ToDo.objects.filter(task_description="Prepare for exams").exists())

    def test_edit_todo_view(self):
        self.client.login(username="student1", password="password123")
        response = self.client.post(reverse("edit_todo", args=[self.todo.id]), {
            "task_description": "Updated project",
            "deadline": (datetime.now(pytz.UTC) + timedelta(days=4)).strftime("%Y-%m-%dT%H:%M"),
            "status": "Completed"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after edit
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.task_description, "Updated project")
        self.assertEqual(self.todo.status, "Completed")

    def test_delete_todo_view(self):
        self.client.login(username="student1", password="password123")
        response = self.client.post(reverse("delete_todo", args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after delete
        self.assertFalse(ToDo.objects.filter(id=self.todo.id).exists())
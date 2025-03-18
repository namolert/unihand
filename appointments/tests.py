from django.test import TestCase
from django.contrib.auth import get_user_model
from students.models import Student
from professors.models import Professor
from .models import Appointment
from django.utils import timezone
from datetime import timedelta
from .forms import AppointmentForm
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
from students.models import Student
from professors.models import Professor
from programs.models import Program

User = get_user_model()

class AppointmentModelTest(TestCase):

    def setUp(self):
        self.professor = Professor.objects.create(
            user=User.objects.create_user(
                username="prof1", 
                password="password",
                first_name="Alice",
                last_name="Smith",
                email="professor@example.com",
            ),
            professor_id="P12345",
            department="Computer Science"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(
            user=User.objects.create_user(
                username="stud1", 
                password="password",
                first_name="John",
                last_name="Doe",
                email="student@example.com",
            ),
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )
        
        # Create an appointment
        self.appointment = Appointment.objects.create(
            student=self.student,
            professor=self.professor,
            date=timezone.now() + timedelta(days=1),  # Appointment is scheduled for tomorrow
            reason="Test appointment"
        )

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.student, self.student)
        self.assertEqual(self.appointment.professor, self.professor)
        self.assertEqual(self.appointment.status, "Pending")

    def test_appointment_str(self):
        expected_str = f"Appointment with {self.professor.user.get_full_name()} - Pending"
        self.assertEqual(str(self.appointment), expected_str)

    def test_update_status(self):
        self.appointment.status = "Accepted"
        self.appointment.save()
        self.assertEqual(self.appointment.status, "Accepted")

class AppointmentFormTest(TestCase):

    def setUp(self):
        self.professor = Professor.objects.create(
            user=User.objects.create_user(
                username="prof1", 
                password="password",
                first_name="Alice",
                last_name="Smith",
                email="professor@example.com",
            ),
            professor_id="P12345",
            department="Computer Science"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(
            user=User.objects.create_user(
                username="stud1", 
                password="password",
                first_name="John",
                last_name="Doe",
                email="student@example.com",
            ),
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )

    def test_appointment_form_valid(self):
        form_data = {
            "professor": self.professor.id,
            "date": (timezone.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M'),
            "reason": "Test appointment"
        }
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_appointment_form_invalid(self):
        form_data = {
            "professor": self.professor.id,
            "date": "",
            "reason": ""
        }
        form = AppointmentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

class AppointmentRequestViewTest(TestCase):

    def setUp(self):
        self.professor = Professor.objects.create(
            user=User.objects.create_user(
                username="prof1", 
                password="password",
                first_name="Alice",
                last_name="Smith",
                email="professor@example.com",
            ),
            professor_id="P12345",
            department="Computer Science"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(
            user=User.objects.create_user(
                username="stud1", 
                password="password",
                first_name="John",
                last_name="Doe",
                email="student@example.com",
            ),
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )
        self.client = Client()

    def test_request_appointment(self):
        self.client.login(username="stud1", password="password")
        response = self.client.get(reverse("request_appointment"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "appointments/students/request_appointment.html")

    def test_create_appointment(self):
        self.client.login(username="stud1", password="password")
        data = {
            "professor": self.professor.id,
            "date": (timezone.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M'),
            "reason": "Test appointment"
        }
        response = self.client.post(reverse("request_appointment"), data)
        self.assertRedirects(response, reverse("appointments"))
        self.assertEqual(Appointment.objects.count(), 1)

class AppointmentResponseViewTest(TestCase):

    def setUp(self):
        self.professor = Professor.objects.create(
            user=User.objects.create_user(
                username="prof1", 
                password="password",
                first_name="Alice",
                last_name="Smith",
                email="professor@example.com",
            ),
            professor_id="P12345",
            department="Computer Science"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(
            user=User.objects.create_user(
                username="stud1", 
                password="password",
                first_name="John",
                last_name="Doe",
                email="student@example.com",
            ),
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )
        self.appointment = Appointment.objects.create(
            student=self.student,
            professor=self.professor,
            date=timezone.now() + timedelta(days=1),
            reason="Test appointment"
        )
        self.client = Client()

    def test_professor_accept_appointment(self):
        self.client.login(username="prof1", password="password")
        data = {"status": "Accepted"}
        response = self.client.post(reverse("professor_appointments_view"), {"appointment_id": self.appointment.id, **data})
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, "Accepted")

    def test_professor_decline_appointment(self):
        self.client.login(username="prof1", password="password")
        data = {"status": "Declined"}
        response = self.client.post(reverse("professor_appointments_view"), {"appointment_id": self.appointment.id, **data})
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, "Declined")
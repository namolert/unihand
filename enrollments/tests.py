from django.test import TestCase
from django.contrib.auth import get_user_model
from courses.models import Course
from enrollments.models import Enrollment
from django import forms
from .forms import EnrollmentForm
from django.urls import reverse
from django.test import Client
from students.models import Student
from professors.models import Professor
from programs.models import Program
from django.contrib.messages import get_messages


User = get_user_model()

class EnrollmentModelTest(TestCase):

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
        self.student = User.objects.create_user(
            username="stud1", 
            password="password",
            first_name="John",
            last_name="Doe",
            email="student@example.com",
        )
        self.student_profile = Student.objects.create(
            user=self.student,
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )

        self.course = Course.objects.create(
            course_code="CS101", course_name="Computer Science 101", program_code=self.program,
            semester_number=1, course_type="Mandatory", academic_year_added=2025, credits=3
        )
        self.course.professors.add(self.professor)

        self.enrollment = Enrollment.objects.create(
            student=self.student_profile,
            course=self.course,
            created_by=self.professor.user,
        )

    def test_enrollment_creation(self):
        self.assertEqual(self.enrollment.student, self.student_profile)
        self.assertEqual(self.enrollment.course, self.course)
        self.assertEqual(self.enrollment.created_by, self.professor.user)
        self.assertTrue(self.enrollment.is_active)

    def test_enrollment_str(self):
        expected_str = f"{self.student_profile.student_id} - {self.course.course_code}"
        self.assertEqual(str(self.enrollment), expected_str)

class EnrollmentFormTest(TestCase):

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
        self.student = User.objects.create_user(
            username="stud1", 
            password="password",
            first_name="John",
            last_name="Doe",
            email="student@example.com",
        )
        self.student_profile = Student.objects.create(
            user=self.student,
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )

        self.course = Course.objects.create(
            course_code="CS101", course_name="Computer Science 101", program_code=self.program,
            semester_number=1, course_type="Mandatory", academic_year_added=2025, credits=3
        )
        self.course.professors.add(self.professor)

    def test_enrollment_form_valid(self):
        form_data = {
            'student': self.student_profile.id
        }
        form = EnrollmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_enrollment_form_invalid(self):
        form_data = {
            'student': ''
        }
        form = EnrollmentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('student', form.errors)

class EnrolledClassesViewTest(TestCase):

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
        self.student = User.objects.create_user(
            username="stud1", 
            password="password",
            first_name="John",
            last_name="Doe",
            email="student@example.com",
        )
        self.student_profile = Student.objects.create(
            user=self.student,
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )

        self.course = Course.objects.create(
            course_code="CS101", course_name="Computer Science 101", program_code=self.program,
            semester_number=1, course_type="Mandatory", academic_year_added=2025, credits=3
        )
        self.course.professors.add(self.professor)
        self.enrollment = Enrollment.objects.create(student=self.student_profile, course=self.course, created_by=self.professor.user)

        self.client = Client()

    def test_enrolled_classes_view(self):
        self.client.login(username="stud1", password="password")
        response = self.client.get(reverse("enrolled_classes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "enrollments/students/enrolled_classes.html")
        self.assertContains(response, "Computer Science 101")

class EnrolledStudentsViewTest(TestCase):

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
        self.student = User.objects.create_user(
            username="stud1", 
            password="password",
            first_name="John",
            last_name="Doe",
            email="student@example.com",
        )
        self.student_profile = Student.objects.create(
            user=self.student,
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )

        self.course = Course.objects.create(
            course_code="CS101", course_name="Computer Science 101", program_code=self.program,
            semester_number=1, course_type="Mandatory", academic_year_added=2025, credits=3
        )
        self.course.professors.add(self.professor)
        self.enrollment = Enrollment.objects.create(student=self.student_profile, course=self.course, created_by=self.professor.user)

        self.client = Client()

    def test_enrolled_students_view(self):
        self.client.login(username="prof1", password="password")
        response = self.client.get(reverse("enrolled_students"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "enrollments/professors/enrolled_students.html")
        self.assertContains(response, "John Doe")

class EnrollingViewTest(TestCase):

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
        self.student = User.objects.create_user(
            username="stud1", 
            password="password",
            first_name="John",
            last_name="Doe",
            email="student@example.com",
        )
        self.student_profile = Student.objects.create(
            user=self.student,
            student_id="S12345",
            program_code=self.program,
            gpa=3.5,
            status="ResultAwaiting"
        )

        self.course = Course.objects.create(
            course_code="CS101", course_name="Computer Science 101", program_code=self.program,
            semester_number=1, course_type="Mandatory", academic_year_added=2025, credits=3
        )
        self.course.professors.add(self.professor)
        self.enrollment = Enrollment.objects.create(student=self.student_profile, course=self.course, created_by=self.professor.user.username)
        self.client = Client()

    def test_enroll_student_in_course(self):
        self.client.login(username="prof1", password="password")
        response = self.client.post(reverse("enrolling", args=[self.course.course_id]), {'student': self.student_profile.id})
        self.assertRedirects(response, reverse("enrolled_students"))
        self.assertEqual(Enrollment.objects.count(), 1)

    # def test_enroll_student_in_course_already_enrolled(self):
    #     self.client.login(username="stud1", password="password")
    #     response = self.client.post(reverse("enrolling", kwargs={"course_id": self.course.course_id}), {
    #         'student': self.student_profile.id,
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse("enrolled_students"))
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(str(messages[0]), "Student is already enrolled in this course.")

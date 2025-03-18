from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from schedules.models import CourseSchedule
from courses.models import Course
from programs.models import Program
from professors.models import Professor
from enrollments.models import Enrollment
from students.models import Student
import pytz
from django.urls import reverse

User = get_user_model()

class CourseScheduleModelTest(TestCase):

    def setUp(self):
        self.professor_user = User.objects.create_user(
            username="prof1",
            password="password",
            first_name="Alice",
            last_name="Smith",
            email="professor@example.com"
        )
        self.professor = Professor.objects.create(user=self.professor_user, professor_id="P12345", department="CS")

        self.student_user = User.objects.create_user(
            username="stud1",
            password="password",
            first_name="John",
            last_name="Doe",
            email="student@example.com"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(user=self.student_user, student_id="S12345", program_code=self.program, gpa=3.5, status="Active")

        self.course = Course.objects.create(
            course_code="CS101",
            course_name="Introduction to Computer Science",
            program_code=self.program,
            semester_number=1,
            course_type="Mandatory",
            academic_year_added=2025,
            credits=3
        )
        self.course.professors.add(self.professor)

        self.enrollment = Enrollment.objects.create(student=self.student, course=self.course, created_by=self.professor_user.username)

        self.course_schedule = CourseSchedule.objects.create(
            academic_year="2025-2026",
            course=self.course,
            professor=self.professor,
            is_scheduled=True,
            is_online=False,
            schedule_start=datetime(2025, 3, 1, 10, 0, tzinfo=pytz.UTC),
            schedule_end=datetime(2025, 3, 1, 12, 0, tzinfo=pytz.UTC),
            course_type="Lecture",
            created_by="admin"
        )

    def test_course_schedule_creation(self):
        """Test if course schedule is created correctly"""
        self.assertEqual(self.course_schedule.academic_year, "2025-2026")
        self.assertEqual(self.course_schedule.course, self.course)
        self.assertEqual(self.course_schedule.professor, self.professor)
        self.assertTrue(self.course_schedule.is_scheduled)
        self.assertFalse(self.course_schedule.is_online)

    def test_course_schedule_str(self):
        """Test the string representation of CourseSchedule"""
        expected_str = f"{self.course.course_name} ({self.course_schedule.academic_year}) - {self.professor_user.get_full_name()}"
        self.assertEqual(str(self.course_schedule), expected_str)


class CourseScheduleViewTest(TestCase):

    def setUp(self):
        self.professor_user = User.objects.create_user(
            username="prof1",
            password="password",
            first_name="Alice",
            last_name="Smith",
            email="professor@example.com"
        )
        self.professor = Professor.objects.create(user=self.professor_user, professor_id="P12345", department="CS")

        self.student_user = User.objects.create_user(
            username="stud1",
            password="password",
            first_name="John",
            last_name="Doe",
            email="student@example.com"
        )
        self.program = Program.objects.create(program_name="Computer Science", program_code="CS")
        self.student = Student.objects.create(user=self.student_user, student_id="S12345", program_code=self.program, gpa=3.5, status="Active")

        self.course = Course.objects.create(
            course_code="CS101",
            course_name="Intro to CS",
            program_code=self.program,
            semester_number=1,
            course_type="Mandatory",
            academic_year_added=2025,
            credits=3
        )
        self.course.professors.add(self.professor)

        self.enrollment = Enrollment.objects.create(student=self.student, course=self.course, created_by=self.professor_user.username)

        self.course_schedule = CourseSchedule.objects.create(
            academic_year="2025-2026",
            course=self.course,
            professor=self.professor,
            is_scheduled=True,
            is_online=False,
            schedule_start=datetime(2025, 3, 1, 10, 0, tzinfo=pytz.UTC),
            schedule_end=datetime(2025, 3, 1, 12, 0, tzinfo=pytz.UTC),
            course_type="Lecture",
            created_by="admin"
        )

    def test_student_course_schedule_view(self):
        self.client.login(username="stud1", password="password")
        response = self.client.get(reverse("student_course_schedule"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Intro to CS")

    def test_professor_course_schedule_view(self):
        self.client.login(username="prof1", password="password")
        response = self.client.get(reverse("professor_course_schedule"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Intro to CS")

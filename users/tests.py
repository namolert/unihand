from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.forms import RegisterForm, LoginForm
from users.permissions import is_student, is_professor, is_admin
from django.core.exceptions import PermissionDenied

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123',
            role='Student'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword123'))
        self.assertEqual(self.user.role, 'Student')
    
    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser (Student)')


class RegisterFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': '',
            'email': 'invalidemail',
            'password1': 'pass',
            'password2': 'pass123',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())


class LoginFormTest(TestCase):
    def test_valid_login_form(self):
        form = LoginForm(data={'username': 'testuser', 'password': 'testpassword123'})
        self.assertTrue(form.is_valid())
    
    def test_invalid_login_form(self):
        form = LoginForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())


class PermissionTest(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(
            username='student', email='student@example.com', role='Student', password='testpass'
        )
        self.professor = User.objects.create_user(
            username='professor', email='professor@example.com', role='Professor', password='testpass'
        )
        self.admin = User.objects.create_user(
            username='admin', email='admin@example.com', role='Admin', password='testpass'
        )
        self.guest = User.objects.create_user(
            username='guest', email='guest@example.com', role='Guest', password='testpass'
        )

    def test_is_student(self):
        self.assertRaises(PermissionDenied, is_student, self.guest)
        is_student(self.student)  # Should not raise an error

    def test_is_professor(self):
        self.assertRaises(PermissionDenied, is_professor, self.guest)
        is_professor(self.professor)  # Should not raise an error

    def test_is_admin(self):
        self.assertRaises(PermissionDenied, is_admin, self.guest)
        is_admin(self.admin)  # Should not raise an error


class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword123', role='Student')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword123'})
        self.assertEqual(response.status_code, 302)  # Redirect on successful login

    def test_invalid_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Stay on the same page

    def test_role_based_redirect(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('role_redirect'))
        self.assertEqual(response.status_code, 302)  # Should redirect based on role

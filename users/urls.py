from django.urls import include, path
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("role-redirect/", views.role_based_redirect, name="role_redirect"),
    path("student/home/", views.student_home, name="student_home"),
    path("professor/home/", views.professor_home, name="professor_home"),
    path("admin/home/", views.admin_home, name="admin_home"),
]
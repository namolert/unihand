from django.urls import path
from . import views

urlpatterns = [
    path("", views.appointments_view, name="appointments"),
    path("request/", views.request_appointment_view, name="request_appointment"),
    path("professor/", views.professor_appointments_view, name="professor_appointments_view"),
    path("accept/<int:appointment_id>/", views.accept_appointment, name="accept_appointment"),
    path("decline/<int:appointment_id>/", views.decline_appointment, name="decline_appointment"),
]
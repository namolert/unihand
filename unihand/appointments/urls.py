from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointments_view, name='appointments'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollments_view, name='enrollments'),
]
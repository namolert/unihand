from django.urls import path
from . import views

urlpatterns = [
    path('', views.grades_view, name="grades"),
]
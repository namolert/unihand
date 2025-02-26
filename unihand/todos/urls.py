from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_view, name="todos"),
]

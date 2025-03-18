from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_view, name="todos"),
    path("edit/<int:todo_id>/", views.edit_todo_view, name="edit_todo"),
    path("delete/<int:todo_id>/", views.delete_todo_view, name="delete_todo"),
]

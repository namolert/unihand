from django.db import models
from students.models import Student

class ToDo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="todos")
    task_description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('Not Start', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Start')

    def __str__(self):
        return f"{self.task_description} ({self.status})"

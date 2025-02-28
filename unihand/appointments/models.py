from django.db import models
from django.contrib.auth import get_user_model
from students.models import Student
from professors.models import Professor

User = get_user_model()

class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="appointments")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateTimeField()
    reason = models.TextField(default="No reason provided")

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Declined", "Declined"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.professor.user.get_full_name()} - {self.status}"
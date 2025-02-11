from django.db import models
from users.models import User

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="professor")
    professor_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.professor_id})"

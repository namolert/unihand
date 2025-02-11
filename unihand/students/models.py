from django.db import models
from users.models import User
from programs.models import Program

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    student_id = models.CharField(max_length=20, unique=True)
    program_code = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="students")
    gpa = models.FloatField(null=True, blank=True)

    STATUS_CHOICES = [
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
        ('ResultAwaiting', 'Result Awaiting'),
        ('Expelled', 'Expelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ResultAwaiting')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.student_id})"

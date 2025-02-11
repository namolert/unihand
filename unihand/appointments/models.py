from django.db import models
from students.models import Student
from professors.models import Professor

class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="appointments")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="appointments")
    appointment_time = models.DateTimeField()
    
    STATUS_CHOICES = [
        ('Incomplete', 'Incomplete'),
        ('Completed', 'Completed'),
        ('Cancel', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Incomplete')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_id} - {self.professor.professor_id} ({self.status})"

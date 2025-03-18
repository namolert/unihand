from django.db import models
from courses.models import Course
from students.models import Student
from programs.models import Program
from users.models import User

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="grades", null=True, blank=True)
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'Professor'})
    
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
        ('Incomplete', 'Incomplete'),
    ]
    
    grade = models.CharField(max_length=12, choices=GRADE_CHOICES)
    comments = models.TextField(null=True, blank=True)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.course_name} - {self.grade}"

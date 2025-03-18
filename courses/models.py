from django.db import models
from programs.models import Program
from professors.models import Professor

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=255)
    program_code = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="courses")
    semester_number = models.PositiveIntegerField()

    COURSE_TYPE_CHOICES = [
        ('Mandatory', 'Mandatory'),
        ('Elective', 'Elective'),
    ]
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES)
    credits = models.PositiveIntegerField(default=3)
    academic_year_added = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    professors = models.ManyToManyField(Professor, related_name="courses_taught")

    def __str__(self):
        return f"{self.course_code} - {self.course_name} ({self.program_code.program_name})"

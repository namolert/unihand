from django.db import models
from courses.models import Course

class CourseSchedule(models.Model):
    academic_year = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="schedules")
    is_scheduled = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    schedule_start = models.DateTimeField()
    schedule_end = models.DateTimeField()
    recurrence_rule = models.TextField(null=True, blank=True)
    
    COURSE_TYPE_CHOICES = [
        ('Lab', 'Lab'),
        ('Lecture', 'Lecture'),
    ]
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES)
    
    link = models.URLField(null=True, blank=True)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=255, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.course.course_code} - {self.academic_year}"

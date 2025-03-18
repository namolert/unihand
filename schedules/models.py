from django.db import models
from courses.models import Course
from professors.models import Professor
from recurrence.fields import RecurrenceField
from dateutil import rrule
from datetime import datetime, timedelta
import pytz

class CourseSchedule(models.Model):
    academic_year = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="schedules")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="schedules", null=True, blank=True)
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

    def get_recurring_schedule(self):
        if self.recurrence_rule:
            try:
                end_date = self.schedule_start + timedelta(days=20)
                until_str = end_date.strftime("%Y%m%dT235959Z")
                if "UNTIL=" not in self.recurrence_rule:
                    recurrence_with_until = f"{self.recurrence_rule};UNTIL={until_str}"
                else:
                    recurrence_with_until = self.recurrence_rule

                rule = rrule.rrulestr(recurrence_with_until, dtstart=self.schedule_start)
                return list(rule)[:2]
            
            except ValueError as e:
                print(f"Error parsing recurrence rule: {e}")
                return []
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return []
        return []

    def __str__(self):
        return f"{self.course.course_name} ({self.academic_year}) - {self.professor.user.get_full_name()}"

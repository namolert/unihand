from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user', 'program_code', 'gpa', 'status')
    search_fields = ('student_id', 'user__username')
    list_filter = ('status', 'program_code')
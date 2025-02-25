from django.contrib import admin
from .models import Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "program", "grade", "professor", "date_recorded")
    list_filter = ("program", "grade")
    search_fields = ("student__user__username", "professor__username")
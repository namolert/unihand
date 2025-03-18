from django.contrib import admin
from .models import Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "grade", "professor", "date_recorded")
    list_filter = ("course", "grade")
    search_fields = ("student__user__username", "professor__username")
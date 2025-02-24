from django.contrib import admin
from .models import Professor

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('professor_id', 'user', 'department')
    search_fields = ('professor_id', 'user__username', 'department')

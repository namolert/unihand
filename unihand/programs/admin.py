from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_code', 'program_name')
    search_fields = ('program_code', 'program_name')

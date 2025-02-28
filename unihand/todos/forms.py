from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["task_description", "deadline", "status"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

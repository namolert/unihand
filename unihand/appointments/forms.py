from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["professor", "date", "reason"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "reason": forms.Textarea(attrs={"rows": 3}),
        }

class AppointmentResponseForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["status"]

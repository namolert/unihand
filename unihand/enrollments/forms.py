from django import forms
from enrollments.models import Enrollment
from students.models import Student

class EnrollmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Select a Student")

    class Meta:
        model = Enrollment
        fields = ["student"]

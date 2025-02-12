from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=User.GENDER_CHOICES, required=False)
    joined_year = forms.IntegerField(required=False)
    left_year = forms.IntegerField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth', 'gender', 'joined_year', 'left_year', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'Student'  # Default role assigned
        if commit:
            user.save()
        return user
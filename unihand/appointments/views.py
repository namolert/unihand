from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def appointments_view(request):
    return render(request, "appointments/appointments.html")

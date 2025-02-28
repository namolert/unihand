from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm, AppointmentResponseForm

@login_required
def appointments_view(request):
    if request.user.role == "Student":
        appointments = Appointment.objects.filter(student=request.user.student)
    elif request.user.role == "Professor":
        appointments = Appointment.objects.filter(professor=request.user.professor)
    else:
        appointments = []

    return render(request, "appointments/appointments.html", {"appointments": appointments})

@login_required
def request_appointment_view(request):
    if not hasattr(request.user, "student"):
        return redirect("home")

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.student = request.user.student
            appointment.save()
            return redirect("appointments")
    else:
        form = AppointmentForm()

    return render(request, "appointments/students/request_appointment.html", {"form": form})

@login_required
def professor_appointments_view(request):
    if not hasattr(request.user, "professor"):
        return redirect("home")

    appointments = Appointment.objects.filter(professor=request.user.professor)

    if request.method == "POST":
        appointment = get_object_or_404(Appointment, id=request.POST.get("appointment_id"))
        form = AppointmentResponseForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect("professor_appointments_view")
    
    return render(request, "appointments/professors/view_appointments.html", {"appointments": appointments})

@login_required
def accept_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, professor=request.user.professor)
    appointment.status = "Accepted"
    appointment.save()
    messages.success(request, "Appointment accepted!")
    return redirect("appointments")

@login_required
def decline_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, professor=request.user.professor)
    appointment.status = "Declined"
    appointment.save()
    messages.error(request, "Appointment declined.")
    return redirect("appointments")

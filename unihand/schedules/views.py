from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def course_schedules_view(request):
    return render(request, "schedules/schedules.html")
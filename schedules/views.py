from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment
from schedules.models import CourseSchedule
from appointments.models import Appointment
from datetime import datetime
from django.utils import timezone
from datetime import timedelta

@login_required
def student_course_schedule(request):
    student = request.user.student  
    # course_schedule = CourseSchedule.objects.filter(course__enrollments__student=student)

    week_offset = request.GET.get('week_offset', '0')  # Default to 0 if not provided
    try:
        week_offset = int(week_offset)  # Convert to int
    except ValueError:
        week_offset = 0  # If conversion fails, fallback to 0

    current_date = timezone.now()
    start_of_week = current_date - timedelta(days=current_date.weekday()) + timedelta(weeks=week_offset)
    end_of_week = start_of_week + timedelta(days=6)

    # Set time to 00:00:00 for start_of_week and end_of_week
    start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_week = end_of_week.replace(hour=23, minute=59, second=59, microsecond=999999)

    # Fetch all courses taught by the professor for the given week
    course_schedule = CourseSchedule.objects.filter(
        course__enrollments__student=student,
        schedule_start__gte=start_of_week,
        schedule_end__lte=end_of_week
    )

    time_slots = [
        "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"
    ]
    days_of_week = [
        "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ]

    week_schedule = []
    for day in days_of_week:
        week_schedule.append({
            'day': day,
            'schedules': []
        })

    day_dict = {
        "MO": "Monday", "TU": "Tuesday", "WE": "Wednesday", "TH": "Thursday", "FR": "Friday", "SA": "Saturday", "SU": "Sunday"
    }

    for schedule in course_schedule:
        # No recurrence rule, treat each schedule as one-time
        day_name = schedule.schedule_start.strftime('%A')  # Get the day of the week name from schedule_start
        # Find the correct day in the week_schedule and append the schedule to it
        for day_entry in week_schedule:
            if day_entry['day'] == day_name:
                day_entry['schedules'].append({
                    "schedule_id": schedule.id,
                    "schedule_time": schedule.schedule_start,
                    "schedule_end": schedule.schedule_end,
                    "duration": (schedule.schedule_end - schedule.schedule_start).seconds // 3600, 
                    "professor_name": schedule.professor.user.get_full_name,
                    "course_name": schedule.course.course_name,
                    "course_id": schedule.course.course_id,
                    "course_type": schedule.course_type
                })
    

    confirmed_appointment = Appointment.objects.filter(
        student=student,
        date__gte=start_of_week,
        date__lte=end_of_week
    )

    for schedule in confirmed_appointment:
        # No recurrence rule, treat each schedule as one-time
        day_name = schedule.date.strftime('%A')  # Get the day of the week name from schedule_start
        # Find the correct day in the week_schedule and append the schedule to it
        for day_entry in week_schedule:
            if day_entry['day'] == day_name:
                day_entry['schedules'].append({
                    "schedule_id": None,
                    "schedule_time": schedule.date,
                    "schedule_end": schedule.date,
                    "duration": 1, 
                    "professor_name": schedule.professor.user.get_full_name,
                    "course_name": schedule.professor.user.get_full_name,
                    "course_id": -1,
                    "course_type": "Appointment"
                })
    
    # Now we need to merge and sort all schedules for each day
    for day_entry in week_schedule:
        # Sort the schedules by the start time
        day_entry['schedules'] = sorted(day_entry['schedules'], key=lambda x: x['schedule_time'])

    # List of days of the week
    context = {
        "course_schedule": course_schedule,
        "student_appointment": confirmed_appointment,
        "time_slots": time_slots,
        "days_of_week": days_of_week,
        "week_schedule": week_schedule,
        "week_offset": week_offset,
        "end_of_week": end_of_week,
        "start_of_week": start_of_week
    }
    return render(request, "schedules/students/course_schedule.html", context)

@login_required
def professor_course_schedule(request):
    professor = request.user.professor
    # Get the current week or a specific week based on GET parameters
    week_offset = request.GET.get('week_offset', '0')  # Default to 0 if not provided
    try:
        week_offset = int(week_offset)  # Convert to int
    except ValueError:
        week_offset = 0  # If conversion fails, fallback to 0

    current_date = timezone.now()
    start_of_week = current_date - timedelta(days=current_date.weekday()) + timedelta(weeks=week_offset)
    end_of_week = start_of_week + timedelta(days=6)

    # Set time to 00:00:00 for start_of_week and end_of_week
    start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_week = end_of_week.replace(hour=23, minute=59, second=59, microsecond=999999)

    # Fetch all courses taught by the professor for the given week
    course_schedule = CourseSchedule.objects.filter(
        professor=professor,
        schedule_start__gte=start_of_week,
        schedule_end__lte=end_of_week
    )

    time_slots = [
        "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"
    ]
    days_of_week = [
        "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ]

    week_schedule = []
    for day in days_of_week:
        week_schedule.append({
            'day': day,
            'schedules': []
        })

    day_dict = {
        "MO": "Monday", "TU": "Tuesday", "WE": "Wednesday", "TH": "Thursday", "FR": "Friday", "SA": "Saturday", "SU": "Sunday"
    }

    # Process each schedule
    for schedule in course_schedule:
        # No recurrence rule, treat each schedule as one-time
        day_name = schedule.schedule_start.strftime('%A')  # Get the day of the week name from schedule_start
        # Find the correct day in the week_schedule and append the schedule to it
        for day_entry in week_schedule:
            if day_entry['day'] == day_name:
                day_entry['schedules'].append({
                    "schedule_id": schedule.id,
                    "schedule_time": schedule.schedule_start,
                    "schedule_end": schedule.schedule_end,
                    "duration": (schedule.schedule_end - schedule.schedule_start).seconds // 3600, 
                    "professor_name": schedule.professor.user.get_full_name,
                    "course_name": schedule.course.course_name,
                    "course_id": schedule.course.course_id,
                    "course_type": schedule.course_type
                })

    # List of days of the week
    context = {
        "course_schedule": course_schedule,
        "time_slots": time_slots,
        "days_of_week": days_of_week,
        "week_schedule": week_schedule,
        "week_offset": week_offset,
        "end_of_week": end_of_week,
        "start_of_week": start_of_week
    }
    
    return render(request, "schedules/professors/course_schedule.html", context)

@login_required
def edit_class_schedule(request, schedule_id):
    # Get the specific schedule to edit
    schedule = get_object_or_404(CourseSchedule, id=schedule_id)
    
    if request.method == "POST":
        # Handle the form submission to update the schedule
        schedule.course_name = request.POST.get("course_name")
        schedule.professor_name = request.POST.get("professor")  # If you plan to allow changes here
       
        # Parsing the datetime-local input values
        try:
            new_start_time = request.POST.get("new_start_time")
            new_end_time = request.POST.get("new_end_time")

            # Convert the string from the datetime-local input to datetime objects
            schedule.schedule_start = datetime.strptime(new_start_time, "%Y-%m-%dT%H:%M")
            schedule.schedule_end = datetime.strptime(new_end_time, "%Y-%m-%dT%H:%M")
            
            schedule.save()

            # Redirect to the professor's schedule page
            return redirect('professor_course_schedule')
        except ValueError:
            # If the conversion fails (e.g., missing values), you can handle it here
            # For now, just print an error message (you can also use flash messages or return a validation error)
            print("Invalid date-time format")
            # Optionally, you can render a message to the professor here if there's an error
            return render(request, 'schedules/professors/edit_schedule.html', {'schedule': schedule, 'error': "Invalid date-time format."})

    context = {
        'schedule': schedule
    }
    return render(request, 'schedules/professors/edit_schedule.html', context)

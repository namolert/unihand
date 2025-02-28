mock_programs = [
    {"program_code": "CS101", "program_name": "Computer Science"},
    {"program_code": "EE102", "program_name": "Electrical Engineering"},
    {"program_code": "ME103", "program_name": "Mechanical Engineering"},
]

mock_users = [
    {"username": "mockstudent", "email": "student@example.com", "password": "student123", "role": "Student", "first_name": "John", "last_name": "Doe"},
    {"username": "mockprofessor", "email": "professor@example.com", "password": "professor123", "role": "Professor", "first_name": "Alice", "last_name": "Smith"},
    {"username": "mockadmin", "email": "admin@example.com", "password": "admin123", "role": "Admin", "first_name": "Robert", "last_name": "Brown"},
]

mock_courses = [
    {"course_code": "CS201", "course_name": "Machine Learning", "program_code": "CS101", "semester_number": 2, "course_type": "Mandatory", "credits": 3, "academic_year_added": 2024},
    {"course_code": "CS202", "course_name": "Web Science", "program_code": "CS101", "semester_number": 3, "course_type": "Mandatory", "credits": 4, "academic_year_added": 2024},
    {"course_code": "EE201", "course_name": "Circuit Analysis", "program_code": "EE102", "semester_number": 2, "course_type": "Mandatory", "credits": 3, "academic_year_added": 2023},
    {"course_code": "ME201", "course_name": "Thermodynamics", "program_code": "ME103", "semester_number": 3, "course_type": "Mandatory", "credits": 4, "academic_year_added": 2023},
]

mock_enrollments = [
    {"student_username": "mockstudent", "course_code": "CS201", "created_by": "mockadmin"},
    {"student_username": "mockstudent", "course_code": "CS202", "created_by": "mockadmin"},
]

mock_grades = [
    {"student_username": "mockstudent", "course_code": "CS201", "professor_username": "mockprofessor", "grade": "A", "comments": "Excellent work"},
    {"student_username": "mockstudent", "course_code": "CS202", "professor_username": "mockprofessor", "grade": "B", "comments": "Good effort"},
]

mock_schedules = [
    {
        "academic_year": "2024-2025",
        "course_code": "CS201",
        "professor_username": "mockprofessor",
        "is_scheduled": True,
        "is_online": False,
        "schedule_start": "2024-09-01T09:00:00Z",
        "schedule_end": "2024-09-01T10:30:00Z",
        "course_type": "Lecture",
        "created_by": "mockadmin",
        "recurrence_rule": "FREQ=WEEKLY;BYDAY=TU,TH;BYHOUR=9;BYMINUTE=0;BYSECOND=0"  # Every Tuesday and Thursday at 9 AM
    },
    {
        "academic_year": "2024-2025",
        "course_code": "CS202",
        "professor_username": "mockprofessor",
        "is_scheduled": True,
        "is_online": False,
        "schedule_start": "2024-09-02T11:00:00Z",
        "schedule_end": "2024-09-02T12:30:00Z",
        "course_type": "Lecture",
        "created_by": "mockadmin",
        "recurrence_rule": "FREQ=WEEKLY;BYDAY=MO,WE;BYHOUR=11;BYMINUTE=0;BYSECOND=0"  # Every Monday and Wednesday at 11 AM
    },
]


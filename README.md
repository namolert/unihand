# UniHand

## Overview

UniHand is a webapp designed to make university life easier for the students, professors and management. It acts as a centralized platform for various essential academic functionalities such as

- Module Enrollment
- Class scheduling (For professors to schedule/reschedule classes) (For Students to view upcoming classes)
- Grade viewing and Publishing (Viewing for Students, Publishing for Professors)
- To-do lists (Personal Student activity tracker)
- Appointment scheduling

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Features](#features)
- [API Endpoints](#api-endpoints)

## Installation

### Prerequisites

- Python 3.7+
- Django 3.2+
- PostgreSQL (or SQLite for development)

### Installing Dependencies

To install all dependencies at once, create a `requirements.txt` file with the following content

```
TBA
```

Then install everything with

```
pip install -r requirements.txt
```

## Configuration

### Configure Environment Variables

Create a .env file in the root directory and add environment variables:

```
TBA
```

### Set Up the Database

Run migrations to set up the database schema:

```
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```
python manage.py createsuperuser
```

### Start the development server

```
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to access the application.

## Technologies Used

- **Backend:** Django, Django Rest Framework
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (for development), PostgreSQL (for production)
- **Authentication:** Django's built-in system
- **API:** Django Rest Framework (DRF)

## Features

### User authentication & Security

- Secure login with role-based access control (RBAC) ensures users access only their relevant features.
- Encrypted password storage protects sensitive data.

### Course & Enrollment Management (Simplifies Course Administration)

- Students: View enrolled courses effortlessly.
- Professors: Enroll/remove students in courses as needed.
- Admins: Create, modify, and delete course records.

### Class Scheduling (Keeps Schedules Organized)

- Students: Access up-to-date class timetables.
- Professors: Modify schedules when necessary.
- Admins: Create/delete schedules for effective time management.

### Grade Management (Enhances Transparency & Accessibility)

- Students: View grades in real-time.
- Professors: Input and update student grades easily.
- Admins: Modify grades for corrections when required.

### To-Do List (Students Only) (Improves Organization & Productivity)

- Allows students to track assignments and deadlines, improving time management.

### Appointments (Students & Professors) (Streamlines Communication)

- Enables scheduling/cancelling of meetings for academic discussions.

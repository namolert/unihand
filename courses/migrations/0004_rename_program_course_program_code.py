# Generated by Django 5.1.1 on 2025-02-27 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_professors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='program',
            new_name='program_code',
        ),
    ]

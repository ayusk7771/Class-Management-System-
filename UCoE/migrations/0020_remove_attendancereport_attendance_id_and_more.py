# Generated by Django 4.1.3 on 2023-03-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("UCoE", "0019_remove_subject_staff_subject_staffs"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendancereport",
            name="attendance_id",
        ),
        migrations.RemoveField(
            model_name="attendancereport",
            name="student_id",
        ),
        migrations.DeleteModel(
            name="Attendance",
        ),
        migrations.DeleteModel(
            name="AttendanceReport",
        ),
    ]

# Generated by Django 4.1 on 2023-05-06 13:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0009_meetup_date_meetup_organizer_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meetup",
            name="date",
        ),
        migrations.RemoveField(
            model_name="meetup",
            name="organizer_email",
        ),
    ]

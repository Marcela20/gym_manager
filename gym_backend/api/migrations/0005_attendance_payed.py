# Generated by Django 4.1.3 on 2022-12-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_attendance_members_attendance_absent_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="payed",
            field=models.ManyToManyField(
                blank=True, related_name="payed", to="api.student"
            ),
        ),
    ]

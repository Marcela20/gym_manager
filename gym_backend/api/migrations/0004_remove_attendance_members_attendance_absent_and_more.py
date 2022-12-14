# Generated by Django 4.1.3 on 2022-12-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_date_subgroups"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendance",
            name="members",
        ),
        migrations.AddField(
            model_name="attendance",
            name="absent",
            field=models.ManyToManyField(
                blank=True, related_name="attendance_absent", to="api.student"
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="late",
            field=models.ManyToManyField(
                blank=True, related_name="attendance_late", to="api.student"
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="present",
            field=models.ManyToManyField(
                blank=True, related_name="attendance_present", to="api.student"
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="present_not_payed",
            field=models.ManyToManyField(
                blank=True, related_name="attendance_not_payed", to="api.student"
            ),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_notes_dates_values_remove_dates_allday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='values',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
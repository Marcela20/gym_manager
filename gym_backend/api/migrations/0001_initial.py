# Generated by Django 4.1.3 on 2022-11-25 10:59

import api.custom_fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOfTheWeek', api.custom_fields.DayOfTheWeekField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=1)),
                ('start_hour', models.TimeField()),
                ('stop_hour', models.TimeField(default='')),
                ('repeat', api.custom_fields.FrequencyField(choices=[('1', 'weekly'), ('2', 'biweekly'), ('3', 'monthly')], max_length=1)),
                ('start', models.DateField(default=django.utils.timezone.now)),
                ('stop', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=240)),
                ('second_name', models.CharField(default='Second name', max_length=240)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=240)),
                ('second_name', models.CharField(default='Second name', max_length=240)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('limit', models.IntegerField(default=10)),
                ('level', models.IntegerField(default=1)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.instructor')),
                ('members', models.ManyToManyField(related_name='members', to='api.student')),
                ('time', models.ManyToManyField(related_name='events', to='api.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.room'),
        ),
    ]

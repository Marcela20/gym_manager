from django.db import models
from django.utils import timezone
from .custom_fields import DayOfTheWeekField, FrequencyField
import pandas as pd

class Student(models.Model):
    name = models.CharField(default="Name", max_length=240)
    second_name = models.CharField(default="Second name", max_length=240)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name} {self.second_name}'
        # TODO what if we have more than one person with this name?


class Instructor(models.Model):
    name = models.CharField(default="Name", max_length=240)
    second_name = models.CharField(default="Second name", max_length=240)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.second_name}'
        # TODO what if we have more than one instructor with this name?


class Room(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Event(models.Model):
    dayOfTheWeek = DayOfTheWeekField()
    start_hour = models.TimeField()
    stop_hour = models.TimeField(default='')
    repeat = FrequencyField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    start = models.DateField(default=timezone.now)
    stop = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.dayOfTheWeek} {self.start_hour} {self.room}'

    @property
    def frequency(self):
        FREQUENCY = {
            '1' : 'DAILY',
            '2' : 'WEEKLY',
            '3' : 'BIWEEKLY',
            '4' : 'MONTHLY',
            '5' : 'YEARLY'
        }
        return FREQUENCY.get(self.repeat)

    @property
    def days(self):
        FREQS  = {
            1: 'MO',
            2: 'TU',
            3: 'WE',
            4: 'TH',
            5: 'FR',
            6: 'SA',
            7: 'SU'
        }
        return FREQS.get(int(self.dayOfTheWeek))

    @property
    def dates(self):
        # TODO only weekly are obsłużone
        FREQS  = {
            1: 'W-MON',
            2: 'W-TUE',
            3: 'W-WED',
            4: 'W-THU',
            5: 'W-FRI',
            6: 'W-SAT',
            7: 'W-SUN'
        }
        return pd.date_range(
            start=self.start, end=self.stop,
            freq=FREQS.get(self.dayOfTheWeek)).strftime('%m/%d/%Y').tolist()




class Group(models.Model):
    name = models.CharField(max_length=20, default='')
    members = models.ManyToManyField(Student, related_name='members')
    limit = models.IntegerField(default=10, null=True)
    level = models.IntegerField(default=1, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Dates(models.Model):
    values = models.JSONField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)


class Attendance(models.Model):
    attendance = models.JSONField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    






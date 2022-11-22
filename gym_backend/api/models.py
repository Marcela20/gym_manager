from django.db import models
from django.utils import timezone
import datetime
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
    hour = models.TimeField()
    repeat = FrequencyField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    start = models.DateField(default=timezone.now)
    stop = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.dayOfTheWeek} {self.hour} {self.room}'

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
    limit = models.IntegerField(default=10)
    level = models.IntegerField(default=1)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    time = models.ManyToManyField(Event, related_name='events')
    # cancelled =  models.DateField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_dates(self):
        dates = []
        if len(self.time.all()) == 1:
            return self.time[0].dates
        for d in self.time.all():
            dates += d.dates
        return dates





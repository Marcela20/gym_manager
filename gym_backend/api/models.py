from django.db import models

class Student(models.Model):
    name = models.CharField(default="Name", max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
        # TODO what if we have more than one person with this name?

class Instructor(models.Model):
    name = models.CharField(default="Name", max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return str(self.name)
        # TODO what if we have more than one instructor with this name?

class Room(models.Model):
    name = models.CharField(max_length=30)
    limit = models.IntegerField(default=10, null=True)

    def __str__(self):
        return str(self.name)

class SubGroup(models.Model):
    attribute_id = models.IntegerField(primary_key=True, default=0)
    hour = models.TimeField(null=True, blank=True)
    members = models.ManyToManyField(Student, related_name='members', blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    @classmethod
    def create(cls, **args):
        subgroup = cls(**args)
        subgroup.save()
        return subgroup

class Group(models.Model):
    name = models.CharField(max_length=20, default='')
    subgroups=models.ManyToManyField(SubGroup, related_name='subgroups', blank=True)
    level = models.IntegerField(default=1, null=True)

    @property
    def members(self):
        return self.subgroups.all().values_list('members', flat=True)
    
class Attendance(models.Model):
    subgroup = models.ForeignKey(SubGroup, null=True, on_delete=models.SET_NULL)
    present = models.ManyToManyField(Student, blank=True, related_name='attendance_present')
    late = models.ManyToManyField(Student, blank=True, related_name='attendance_late')
    present_not_payed = models.ManyToManyField(Student, blank=True, related_name='attendance_not_payed')
    absent = models.ManyToManyField(Student, blank=True, related_name='attendance_absent')
    payed = models.ManyToManyField(Student, blank=True, related_name='payed')



class Date(models.Model):
    date = models.DateField(auto_now_add=False, primary_key=True)
    attendance = models.ManyToManyField(Attendance, related_name='attendance', blank=True)
    subgroups=models.ManyToManyField(SubGroup, related_name='subgroups_dates', blank=True)

    @classmethod
    def create(cls, **args):
        date = cls(**args)
        date.save()
        return date


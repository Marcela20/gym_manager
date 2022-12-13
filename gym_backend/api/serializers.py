from rest_framework import serializers
from .models import Student, Group, Room, Instructor, Date, Attendance, SubGroup
from calendar_groups.models import Calendar

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk', 'name', 'email', 'phone', 'registrationDate')

class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = ('pk', 'name', 'email', 'phone', 'registrationDate')


class SubGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubGroup
        fields = ('attribute_id', 'instructor', 'hour', 'members', 'room')

    def add_member(self, instance, validated_data):
        member = validated_data['member'] # should be instructor id
        instance.members.add(member)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('pk', 'name', 'subgroups', 'level')

    def add_subgroup(self, instance, validated_data):
        subgroups = validated_data['subgroup']
        instance.subgroups.add(subgroups)
        instance.save()
        return instance

class RoomSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('pk', 'name', 'limit')

class DateSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Date
        fields = ('pk', 'attendance', 'subgroups')

    def add_attendance(self, instance, validated_data):
        attendance = validated_data['attendance']
        instance.attendance.add(attendance)
        instance.save()
        return instance

class AttendanceSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ('pk', 'subgroup', 'present', 'absent', 'late', 'present_not_payed', 'absent', 'payed')

    def add_member(self, instance, validated_data):
        member = validated_data['member']
        instance.members.add(member)
        instance.save()
        return instance

class CalendarSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = ('values', 'pk', 'group')


from rest_framework import serializers
from .models import Student, Group, Room, Instructor, Event, Dates


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk', 'name', 'second_name', 'email', 'phone', 'registrationDate')


class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = ('pk', 'name', 'second_name', 'email', 'phone')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('pk', 'name', 'limit', 'level', 'instructor', 'members')

    def add_member(self, instance, validated_data):
        member = validated_data['member'] # should be instructor id
        instance.members.add(member)
        instance.save()
        return instance


class RoomSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('pk', 'name')


class EventSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('pk', 'dayOfTheWeek', 'start_hour', 'stop_hour', 'repeat', 'room', 'start', 'stop')


class DatesSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Dates
        # fields = ('title', 'startDate', 'endDate', 'rRule', 'notes', 'group', 'parentData', 'allDay')
        fields = ('values', 'pk', 'group')


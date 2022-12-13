from .models import Student, Group, Room, Instructor, Date, Attendance, SubGroup
from calendar_groups.models import Calendar
from rest_framework import mixins, generics
from rest_framework.response import Response
from .serializers import CalendarSerialzier, StudentSerializer, GroupSerializer, InstructorSerializer, RoomSerialzier, DateSerialzier, AttendanceSerialzier, SubGroupSerializer
from rest_framework.views import APIView
from rest_framework import status
from .get_dates import get_dates, generate_group_view, generate_dates, get_dates_new


class StudentDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GroupAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GroupDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class InstructorDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class InstructorAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoomDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerialzier

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RoomAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerialzier

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DateDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Date.objects.all()
    serializer_class = RoomSerialzier

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class DateAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Date.objects.all()
    serializer_class = DateSerialzier

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AttendanceDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerialzier

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AttendanceAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerialzier

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SubGroupDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = SubGroup.objects.all()
    serializer_class = SubGroupSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SubGroupAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = SubGroup.objects.all()
    serializer_class = SubGroupSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class CalendarDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView,
                  APIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerialzier

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        group = request.data.get('group', None)
        data = {"values": request.data, "group":group}
        instance = Calendar.objects.get(pk=pk)
        serializer =  CalendarSerialzier(instance, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        if SubGroup.objects.filter(pk=pk).exists():
            SubGroup.objects.get(pk=pk).delete()
        return self.destroy(request, *args, **kwargs)


class CalendarAll(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView,
              APIView):

    queryset = Calendar.objects.all()
    serializer_class = CalendarSerialzier

    def get(self, request, *args, **kwargs):
        if request.GET.get("group"):
            dates = Calendar.objects.all().filter(group=request.GET.get("group"))
            a = get_dates_new(dates)
            group_view = generate_group_view(a, Group.objects.get(pk=request.GET.get('group')))
            return Response(group_view)
        return self.list(request, *args, **kwargs)

    def post(self, request, format=None):
        group = request.data.get('group', None)
        data = {"values": request.data, "group":group}
        serializer = CalendarSerialzier(data=data)
        if serializer.is_valid():
            serializer.save()
            values = serializer.data['values']
            serializer.data['values']['AttributeId'] = serializer.data['pk']
            calendar_objects = Calendar.objects.filter(pk=serializer.data['pk'])
            calendar_objects.update(values=values)
            subgroup = SubGroup.objects.get_or_create(attribute_id=serializer.data['values']['AttributeId'])
            Group.objects.get(pk=group).subgroups.add(serializer.data['values']['AttributeId'])
            series_dates = get_dates(calendar_objects)
            generate_dates(series_dates, subgroup[0].attribute_id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

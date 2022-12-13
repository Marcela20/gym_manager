from django.urls import path
from .viewsets import (
    StudentAll, StudentDetail, GroupDetail,
    GroupAll, RoomAll, RoomDetail,
    InstructorAll, InstructorDetail,
    CalendarAll, CalendarDetail, AttendanceAll, AttendanceDetail, DateAll, DateDetail, SubGroupAll, SubGroupDetail)

urlpatterns = [
    path('api/student/', StudentAll.as_view()),
    path('api/student/<int:pk>', StudentDetail.as_view()),
    path('api/group/<int:pk>', GroupDetail.as_view()),
    path('api/group/', GroupAll.as_view()),
    path('api/room/', RoomAll.as_view()),
    path('api/room/<int:pk>', RoomDetail.as_view()),
    path('api/instructor/<int:pk>', InstructorDetail.as_view()),
    path('api/instructor/', InstructorAll.as_view()),
    path('api/calendar/', CalendarAll.as_view()),
    path('api/calendar/<int:pk>', CalendarDetail.as_view()),
    path('api/attendance/<int:pk>', AttendanceDetail.as_view()),
    path('api/attendance/', AttendanceAll.as_view()),
    path('api/date/<int:pk>', DateDetail.as_view()),
    path('api/date/', DateAll.as_view()),
    path('api/subgroup/<int:pk>', SubGroupDetail.as_view()),
    path('api/subgroup/', SubGroupAll.as_view()),






]

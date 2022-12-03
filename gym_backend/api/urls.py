from django.urls import path
from .viewsets import (
    StudentAll, StudentDetail, GroupDetail,
    GroupAll, RoomAll, RoomDetail,
    InstructorAll, InstructorDetail, EventAll, EventDetail,
    DatesAll, DatesDetail)

urlpatterns = [
    path('api/student/', StudentAll.as_view()),
    path('api/student/<int:pk>', StudentDetail.as_view()),
    path('api/group/<int:pk>', GroupDetail.as_view()),
    path('api/group/', GroupAll.as_view()),
    path('api/room/', RoomAll.as_view()),
    path('api/room/<int:pk>', RoomDetail.as_view()),
    path('api/instructor/<int:pk>', InstructorDetail.as_view()),
    path('api/instructor/', InstructorAll.as_view()),
    path('api/event/', EventAll.as_view()),
    path('api/event/<int:pk>', EventDetail.as_view()),
    path('api/calendar/', DatesAll.as_view()),
    path('api/calendar/<int:pk>', DatesDetail.as_view()),


]

from django.urls import path
from .views import dates, dates_one, new_calendar

urlpatterns = [
    path('api/dates/', dates),
    path('api/dates/<int:pk>', dates_one),
    path('api/new_calendar/', new_calendar)



]

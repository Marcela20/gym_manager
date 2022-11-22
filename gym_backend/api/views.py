from django.http import HttpResponse
from .models import Group
import json

def aa(request):
    a = Group.objects.get(pk=3)
    dates = a.get_dates()
    #     {
    #   title: 'Website Re-Design Plan',
    #   startDate: new Date(2018, 6, 23, 9, 30),
    #   endDate: new Date(2018, 6, 23, 11, 30),
    # }
    return HttpResponse(json.dumps({'dates':dates}))
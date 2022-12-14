from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Group
from .models import Calendar
from datetime import datetime

@api_view(['GET'])
def dates(request):
    """returns all enevents for all groups.
        should be narrowed to a specific date range"""
    dates_jsons = []
    groups = Group.objects.all()
    for group in groups:
        title = group.name
        dates = group.get_dates()  # list like [(start_hour, stop_hour, [date1, date2])...]
        for elem in dates:
            for date in elem[2]:
                date = datetime.strptime(date, '%m/%d/%Y').date()
                start_date = datetime.combine(date, elem[0])
                stop_date = datetime.combine(date, elem[1])

                dates_jsons.append(
                                {
                    'title': title,
                    'startDate': start_date.isoformat(),
                    'endDate': stop_date.isoformat()
                }
                )

    return Response(dates_jsons)

@api_view(['GET'])
def dates(request):
    """returns all enevents for all groups.
        should be narrowed to a specific date range"""
    dates_jsons = []
    groups = Group.objects.all()
    for group in groups:
        title = group.name
        for rule in group.time.all():
            dates_jsons.append(
                    {
                        'title': title,
                        'startDate': datetime.combine(rule.start, rule.start_hour),
                        'endDate': datetime.combine(rule.start, rule.stop_hour),
                        'id': rule.id,
                        'rRule': f'FREQ={rule.frequency};BYDAY={rule.days}',
                    }
                    )
    return Response(dates_jsons)


@api_view(['GET'])
def dates_one(request, pk):
    dates_jsons = []
    group = Group.objects.get(pk=pk)
    title = group.name
    for rule in group.time.all():
        dates_jsons.append(
                {
                    'title': title,
                    'startDate': datetime.combine(rule.start, rule.start_hour),
                    'endDate': datetime.combine(rule.start, rule.stop_hour),
                    'rRule': f'FREQ={rule.frequency};BYDAY={rule.days}',
                    }
                    )
    return Response(dates_jsons)


@api_view(['GET'])
def new_calendar(request):
    """returns all enevents for all groups.
        should be narrowed to a specific date range"""
    dates = list(Calendar.objects.all().values_list('values', flat=True))
    dates_jsons = {'data':dates}
    return Response(dates_jsons)
from django.utils.translation import gettext as _
from django.db import models


class DayOfTheWeekField(models.CharField):
    DAY_OF_THE_WEEK = {
    '1' : _(u'Monday'),
    '2' : _(u'Tuesday'),
    '3' : _(u'Wednesday'),
    '4' : _(u'Thursday'),
    '5' : _(u'Friday'),
    '6' : _(u'Saturday'),
    '7' : _(u'Sunday'),
    }

    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(self.DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)

class FrequencyField(models.CharField):
    FREQUENCY = {
    '1' : 'weekly',
    '2' : 'biweekly',
    '3' : 'monthly',
    }

    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(self.FREQUENCY.items()))
        kwargs['max_length']=1
        super(FrequencyField,self).__init__(*args, **kwargs)
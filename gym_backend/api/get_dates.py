import pandas as pd
import json
from .models import Student, Date


def handle_reccurence(d):
    POSSIBLE_REC_VALS = ['FREQ', 'BYDAY', 'BYMONTHDAY', 'COUNT', 'INTERVAL', 'UNTIL', 'BYMONTH']
    POSSIBLE_FREQS = ['HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'YEARLY']
    POSSIBLE_BYDAY = {
            'MO': 'W-MON',
            'TU': 'W-TUE',
            'WE': 'W-WED',
            'TH': 'W-THU',
            'FR': 'W-FRI',
            'SA': 'W-SAT',
            'SU': 'W-SUN'
        }

    MONTHS = {
        1: 'A-JAN',
        2: 'A-FEB',
        3: 'MAR',
        4: 'APR',
        5: 'MAY',
        6: 'JUN',
        7: 'JUL',
        8: 'AUG',
        9: 'SEP',
        10: 'OCT',
        11: 'NOV',
        12: 'DEC'
    }

    periods = d.get('COUNT', None)
    interval = d.get('INTERVAL', '')
    end = d.get('UNTIL', None)

    if periods is None and end is None:
        periods = 50

    if d.get('FREQ') == 'WEEKLY':
        dates = []
        for day in d.get('BYDAY').split(','):
            freq = POSSIBLE_BYDAY.get(day)
            one_daty = {'periods':int(periods), 'end': end, 'freq': f'{interval}{freq}'}
            dates.append(one_daty)
        return({'rec': dates})

    elif d.get('FREQ') == 'MONTHLY':
         freq='MS'
         day = d.get('BYMONTHDAY')
         return({'rec': [{'periods':int(periods), 'end': end, 'freq': f'{interval}{freq}'}], 'delta':pd.Timedelta(days=int(day)-1)})

    elif d.get('FREQ') == 'DAILY':
         freq='D'
         return({'rec': [{'periods':int(periods), 'end': end, 'freq': f'{interval}{freq}'}]})

    elif d.get('FREQ') == 'YEARLY':
        if int(interval) > 5:
            interval = 5  # we cant travel too far in time
        freq = MONTHS.get(int(d.get('BYMONTH')))
        day = d.get('BYMONTHDAY')
        return({'rec': [{'periods': int(periods), 'end': end, 'freq': f'{interval}{freq}'}]})


def get_dates(query):
    all_dates = pd.Series()
    # fields = ['recurrenceException', 'recurrenceRule', 'startDate', 'endDate']
    for entry in query:
        vals = entry.values
        id = entry.id

        start = vals['startDate']
        reccurence = vals.get('recurrenceRule', None)
        if reccurence:
            rec = reccurence.split(';')
            d = {x.split('=')[0]:x.split('=')[1] for x in rec}
            if handle_reccurence(d):
                for dates in handle_reccurence(d)['rec']:
                    all_dates = pd.concat([all_dates, (pd.date_range(start=start, **dates)+ handle_reccurence(d).get('delta', pd.Timedelta(0))).strftime('%Y-%m-%d').to_series()])
        else:
            all_dates = pd.concat([all_dates, pd.date_range(start=start, end=vals['endDate']).strftime('%Y-%m-%d').to_series()])

        if vals.get('recurrenceException'):
            excluded = pd.to_datetime([x for x in vals.get('recurrenceException').split(',')]).to_list()
            for i in excluded:
                all_dates = all_dates.drop(all_dates.loc[all_dates == i].index)
        a = all_dates.to_frame()
        a = a.assign(subgroup=id)
    print(all_dates.T.drop_duplicates().shape)     

    return all_dates.T.drop_duplicates()


def generate_dates(dates, subgroup):
    dates = dates.drop_duplicates()
    for index, date in dates.iteritems():
        new_date = Date.objects.get_or_create(date=date)
        new_date[0].subgroups.add(subgroup)

def generate_group_view(dates, group):

    members_ids = set(group.subgroups.all().values_list('members', flat = True))
    members = Student.objects.filter(id__in=members_ids)
    final_row_data = []
    group_view = pd.DataFrame(index=members, columns=dates.index).fillna(0)
    group_view.index.name = 'students'
    group_view.reset_index(inplace=True)
    group_view = group_view.astype(str)
    data = list(zip(dates.index, dates['subgroup']))
    column_names = [('students', ''), *data]
    dirty = []
    for elem in column_names:
        dirty.append(
            {
            'Header': elem[0],
            'accessor': str(elem[0]),
            'className': "t-cell-1 text-left",
            'subgroup': elem[1], 
            'label': elem[1],
            }
        )
    for index, rows in group_view.iterrows():
        final_row_data.append(rows.to_dict())
    json_result = [{'columns': dirty, 'rowData': json.loads(group_view.to_json(orient='index')).values()}]
    return(json_result)

def get_dates_new(query):
    attendance = pd.DataFrame(columns=['subgroup'])
    # fields = ['recurrenceException', 'recurrenceRule', 'startDate', 'endDate']
    for entry in query:
        vals = entry.values
        id = entry.id

        start = vals['startDate']
        reccurence = vals.get('recurrenceRule', None)
        if reccurence:
            rec = reccurence.split(';')
            d = {x.split('=')[0]:x.split('=')[1] for x in rec}
            if handle_reccurence(d):
                for dates in handle_reccurence(d)['rec']:
                    df = (pd.date_range(start=start, **dates)+ handle_reccurence(d).get('delta', pd.Timedelta(0))).strftime('%Y-%m-%d').to_frame()
                    df = df.assign(subgroup=id)
                    attendance = pd.concat([attendance, 
                    df,
                     ])
        else:
            df = pd.date_range(start=start, end=vals['endDate']).strftime('%Y-%m-%d').to_series()
            df = df.assign(subgroup=id)
            attendance = pd.concat([attendance, df])

        if vals.get('recurrenceException'):
            excluded = pd.to_datetime([x for x in vals.get('recurrenceException').split(',')]).to_list()
            for i in excluded:
                attendance = attendance.drop(attendance.loc[attendance == i].index)

    return attendance
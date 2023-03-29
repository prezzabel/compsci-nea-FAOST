students = {}
year_group = 7
for i in range(10000, 10372):
    students[i] = {
        'name': f'Student {i - 9999}',
        'year_group': year_group,
        'timetable': {
            'mon': {1: '', 2: '', 3: '', 4: '', 5: ''},
            'tues': {1: '', 2: '', 3: '', 4: '', 5: ''},
            'wed': {1: '', 2: '', 3: '', 4: '', 5: ''},
            'thur': {1: '', 2: '', 3: '', 4: '', 5: ''},
            'fri': {1: '', 2: '', 3: '', 4: '', 5: ''}
        }
    }


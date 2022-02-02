def add_time(start, duration, day=None):
    
    ### Variables
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day != None:
        day = day.lower()
        d_ind = days.index(day)
    c_day = ''
    days_later = ''
    d_hour = 0
    c_hour = 0
    minute = 0
    time_change = 0
    day_change = 0
    am_pm = ''
    s = start.split(':')
    x = s[1].split()
    c_hour += int(s[0])
    minute += int(x[0])
    am_pm = x[1]
    d = duration.split(':')
    d_hour += int(d[0])
    minute += int(d[1])
    
    ### Time adding
    while minute > 59:
        if minute > 59:
            minute -= 60
            d_hour += 1
    for i in range(d_hour):
        c_hour += 1
        if c_hour == 12:
            time_change += 1
        if c_hour > 12:
            c_hour -= 12
                
    ### Time Changes (AM/PM)
    if time_change == 1:
        if am_pm == 'AM':
                am_pm = 'PM'
        else:
            am_pm = 'AM'
            day_change += 1
    elif time_change == 0:
        pass
    else:
        for i in range(time_change):
            if am_pm == 'AM':
                am_pm = 'PM'
            else:
                am_pm = 'AM'
                day_change += 1
                
    ### Day Changes
    if day_change > 0:
        if day_change == 1:
            days_later = ' (next day)'
        else:
            days_later = f' ({day_change} days later)'
    
    if day != None:
        if day_change > 0:
            d_ind += day_change
        while d_ind > 6:
            d_ind -= 7
        c_day = f', {days[d_ind].capitalize()}'

    if minute < 10:
        new_time = f'{c_hour}:0{minute} {am_pm}{c_day}{days_later}'
    else:
        new_time = f'{c_hour}:{minute} {am_pm}{c_day}{days_later}'
    return new_time

def add_time(start, duration, *week_day):

    [L, P] = start.split(" ")
    [H, M] = L.split(":")
    [DH, DM] = duration.split(":")
    week_days = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']

    half_day = 12
    ent_day = 24
    day = ''
    days = 0

    new_min = (int(M) + int(DM)) % 60
    new_hour = (int(H) + int(DH)) + (int(M) + int(DM)) // 60

    if P == 'PM':
        new_hour = new_hour + 12
        if new_hour > ent_day:
            days = new_hour // ent_day
            new_hour = new_hour % ent_day
            if days == 1:
                day = '(next day)'
            else:
                day = f'({days} days later)'
    else:
        new_hour = new_hour
        if new_hour > ent_day:
            days = new_hour // ent_day
            new_hour = new_hour % ent_day
            if days == 1:
                day = '(next day)'
            else:
                day = f'({days} days later)'

    if new_hour >= half_day:
        if new_hour == 12:
            new_p = 'PM'
        else:
            new_hour = new_hour - half_day
            new_p = 'PM'

    elif new_hour < half_day:
        new_p = 'AM'
        if new_hour == 0 and new_p == 'AM':
            new_hour += half_day

    if len(str(new_min)) < 2:
        new_min = '0' + str(new_min)
    else:
        new_min = str(new_min)

    count_w_day = 0
    w_day = ''
    sum_w_days = 0
    if week_day:
        week_day = str(week_day).title()

        count_w_day = 0
        for d in week_days:
            if d in week_day:
                w_day = count_w_day
                break
            else:
                count_w_day += 1
        sum_w_days = count_w_day + (days)
        week = (sum_w_days % 7)
        w_day = week_days[week]

        if days > 0:
            new_time = f"{new_hour}:{new_min} {new_p}, {w_day} {day}"
        else:
            new_time = f"{new_hour}:{new_min} {new_p}, {w_day}"

    else:
        if days > 0:
            new_time = f"{new_hour}:{new_min} {new_p} {day}"
        else:
            new_time = f"{new_hour}:{new_min} {new_p}"

    return new_time


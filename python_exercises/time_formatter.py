def time_formatter(time: str):
    new_time = time.split(":")
    hour = int(new_time[0])
    minute = new_time[1]
    second = new_time[2]
    ss = second[:2]
    am_pm = second[-2:]
    if am_pm == 'AM' and hour == 12:
        hour = 0
    elif am_pm == 'PM' and hour < 12:
        hour += 12
    time_2 = str(hour) + ':' + minute + ':' + ss
    return time_2


a = '11:33:23PM'
print(time_formatter(a))


# time = '12:33:32AM'
# new = time.split(":")
# hour = new[0]
# mm = new[1]
# sec = new[2]
# ss = sec[:2]
# am_pm = sec[-2:]
# print(new, hour, mm, sec, ss, am_pm)

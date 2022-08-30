from datetime import datetime

def get_work_week():
    today = datetime.today()
    return today.isocalendar()

def get_remaining_time(dd):
    ww, wd = dd.split('.')
    yr, tw, td = get_work_week()

    rw, rd = 0, 0
    rw = int(ww) - int(tw)
    rd = int(wd) - int(td)

    if rd < 0:
        rw -= 1
        rd = 5 + rd

    result = '-'
    result = str(rw) + '.' + str(rd)
    return result
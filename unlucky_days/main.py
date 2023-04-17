import datetime
from datetime import date

def unlucky_days(year):
    count = 0 
    for i in range(1, 13):
        date = datetime.date(year, i, 13)
        if date.weekday() == 4:
            count += 1
    return count


def unlucky_days_refactored(year):
    return sum(date(year, m, 13).weekday()==4 for m in range(1, 13))

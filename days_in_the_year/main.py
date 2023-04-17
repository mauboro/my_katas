import calendar

def year_days(year):
    return f"{year} has 366 days" if calendar.isleap(year) else f"{year} has 365 days"

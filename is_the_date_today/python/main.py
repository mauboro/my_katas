from datetime import datetime

def is_today(date): 
    return datetime.now().date() == date.date()

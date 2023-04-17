def period_is_late(last,today,cycle_length):
    dt = abs(last - today)
    last = int(dt.__str__().split()[0])
    return last > cycle_length

def period_is_late_refactored(last, today, cycle_length):
    return (today - last).days > cycle_length

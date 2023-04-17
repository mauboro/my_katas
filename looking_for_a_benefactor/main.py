from math import ceil

def new_avg(arr, newavg):
    try:
        if newavg < sum(arr)/len(arr) : raise ValueError
    except ZeroDivisionError:
        pass
    return ceil(((len(arr) + 1) * newavg) - sum(arr))

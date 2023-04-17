def db_sort(arr): 
    numbers = sorted([n for n in arr if isinstance(n, int)])
    strings = sorted([s for s in arr if isinstance(s, str)])
    return numbers + strings

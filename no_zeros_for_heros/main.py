def no_boring_zeros(n):
    return int(str(n).rstrip("0")) if n else 0 

def sum_str(a, b):
    return f"{int(a) + int(b)}" if a and b else f"{int(a) + 0}" if a else f"{int(b) + 0}" if b else "0"

def sum_str_refactored(a, b):
    return str(int(a or 0) + int(b or 0))

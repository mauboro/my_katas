def parse_float(string):
    try:
        return float(string)
    except (TypeError, ValueError):
        return 


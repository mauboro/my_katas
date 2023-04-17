def is_digit(n):
    try:
        if len(n) == 1:
            return int(n) < 10
        else: 
            return 1 == 10
    except ValueError:
        return False


def is_digit_refactored(n):
    return n.isdigit() and len(n) == 1



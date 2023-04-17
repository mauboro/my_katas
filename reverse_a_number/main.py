def reverse_number(n):
    return int(str(n)[::-1]) if str(n)[0] != "-" else int(str(n)[1:][::-1]) * -1



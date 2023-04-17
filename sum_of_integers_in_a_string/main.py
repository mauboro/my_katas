
def sum_of_integers_in_string(s):
    result = 0
    temp = 0
    for char in s:
        if char.isnumeric():
            temp = temp*10 + int(char)
        else:
            result += temp
            temp = 0
    result += temp
    return result

def sum_of_integers_in_string_refactored(s):
    import re

    return sum(map(int, re.findall("\d+", s)))



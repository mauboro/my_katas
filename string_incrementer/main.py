import re

def increment_string(string):
    if not (re.findall("\d+", string)): return string + "1"
    res = (re.findall("\d+", string)[-1])
    return string[:-len(res)] + str((int(res) + 1)).zfill(len(res))

def increment_string_refactored(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

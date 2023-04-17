import re

def check_three_and_two(ar):
    if ar.count("a") == 5 or ar.count("b") == 5: return False
    if re.match(r'^([a-zA-Z])\1{2}([a-zA-Z])\2{1}$', "".join(sorted(ar))) or re.match(r'^([a-zA-Z])\1{1}([a-zA-Z])\2{2}$', "".join(sorted(ar))):
        return True
    else:
        return False

#I said refactored but i guess "made in a human befitting way" is more(ba dum tss) fitting.
def check_three_and_two_refactored(ar):
    return {ar.count(x) for x in set(ar)} == {2, 3}

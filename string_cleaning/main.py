def string_clean(s):
    return "".join([c for c in s if not c.isnumeric()])


#SHORT-CIRCUITING FOR THE WIN BROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoooo
def string_clean_refactored(s):
    from operator import not_

    return "".join([not_(c.isnumeric()) and c or "" for c in s])

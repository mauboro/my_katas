def next_happy_year(year):
    year+=1
    while not all([False if str(year).count(s) > 1 else True for s in str(year)]):
        year += 1
    return year

def next_happy_year_refactored(year):
    year += 1
    while len(set(str(year))) != 4:
        year += 1
    return year



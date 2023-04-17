def nb_year(p0, percent, aug, p):
    years = 1 
    current = p0 + ((p0 * percent) // 100) + aug
    print(current)
    while current < p:
        current += ((current * percent) // 100) + aug
        years += 1
    
    return years if years != 51 else 50
   

def nb_year_recursive(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year_recursive(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years


from math import prod

def even_last(numbers): 
    if not numbers: return False
    return sum([n for i, n in enumerate(numbers) if i % 2 == 0 ]) * numbers[-   1]
    

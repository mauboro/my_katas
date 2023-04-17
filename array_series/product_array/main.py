from math import prod

def product_array(numbers):
    res = []
    for n in numbers:
        res.append(prod(numbers) / n)
    
return res
        

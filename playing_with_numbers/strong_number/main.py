def my_factorial(n):
    if n < 1:
        return 1
    return n * my_factorial(n - 1)

def strong_num(number):
    string = str(number)
    total = 0
    for n in string:
        total +=  my_factorial(int(n))
    
    return "STRONG!!!!" if total == number else "Not Strong !!"

def strong_num_refactored(number):
    from math import factorial 
    return "STRONG!!!!" if sum(factorial(int(n)) for n in str(number)) == number else "Not Strong !!"

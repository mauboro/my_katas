def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for number in range(a, b + 1):
        if sum(int(n)**(i + 1) for i, n in enumerate([n for n in str(number)])) == number:
            result.append(number)
    
    return result
            

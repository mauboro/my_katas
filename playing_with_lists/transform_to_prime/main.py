def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def minimum_number(numbers):
    count = 0 
    while not is_prime(sum(numbers) + count):
        count += 1
    return count
        

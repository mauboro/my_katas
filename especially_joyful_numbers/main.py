def number_joy(n):
    number =  (sum(int(i) for i in str(n))) 
    return number * int(str(number)[::-1]) == n
     

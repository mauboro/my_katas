def give_change(amount): 
    hundredths = 0
    fifties = 0 
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    while amount > 0: 
        if amount >= 100:
            hundredths += 1
            amount -= 100
        elif amount >= 50:
            fifties += 1
            amount -= 50
        elif amount >= 20:
            twenties += 1
            amount -= 20
        elif amount >= 10:
            tens += 1
            amount -= 10
        elif amount >= 5:
            fives += 1
            amount -= 5
        else:
            ones += 1 
            amount -= 1
        
    return (ones, fives, tens, twenties, fifties, hundredths)

def give_change_refactored(amount): 
    arr = []
    for i in [100, 50, 20, 10, 5, 1]:
        arr = [amount // i] + arr
        amount -= arr[0] * i
    return tuple(arr)


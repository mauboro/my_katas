def jumping_number(number):
    if len(str(number)) == 1:
        return "Jumping!!"
    
    count = 0 
    for i, n in enumerate(str(number)):
        if i + 1 == len(str(number)):
            count += 1
            break
        if str(int(n) + 1) == str(number)[i + 1] or str(int(n) - 1) == str(number)[i + 1]:
            count += 1
        else:
            break
    return "Jumping!!" if count == len(str(number)) else "Not!!"

def jumping_number_refactored(number):
    arr = list(map(int, str(number)))
    return ("Not!!", "Jumping")[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]

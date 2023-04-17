def first_non_consecutive(arr):
    previous = arr[0]
    for n in arr[1:]:
        if n != previous + 1:
            return n
        else:
            previous = n
        
       

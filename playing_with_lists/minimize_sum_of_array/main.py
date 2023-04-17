def min_sum(arr):
    arr.sort()
    a = arr[:len(arr)//2][::-1]
    b = arr[len(arr)//2:]
    return sum(map(lambda a, b: a * b, a, b))

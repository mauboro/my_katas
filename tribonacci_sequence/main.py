def tribonacci(signature, n):
    res = signature
    count = 3
    for i in range(n - 3):
        res.append(sum(res[count - 3:]))
        count += 1
    return res if n > 3 else res[:n]

def tribonacci_refactored(signature, n):
    res = signature[:n]
    for i in range(n-3):
        res.append(sum(res[-3:]))
    return res 

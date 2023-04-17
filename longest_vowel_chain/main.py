def solve(s):
    max = 0
    count = 0 
    for c in s:
        if c.lower() in "aeiou":
            count+=1
            if count > max:
                max = count
        else:
            count = 0
    return max

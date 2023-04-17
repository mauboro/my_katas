def calculate_age(b, c):
    if (c - b) == 1:
        return f"You are 1 year old."
    elif (c - b) == -1:
        return f"You will be born in 1 year."
    elif c > b:
        return f"You are {c - b} years old."
    elif c < b:
        return f"You will be born in {abs(c - b)} years."
    elif c == b:
        return f"You were born this very year!"
    

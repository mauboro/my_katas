def second_symbol(s, symbol):
    if symbol not in s: return -1
    count = 0 
    for i, c in enumerate(s):
        if count == 2:
            return i -1
        if c == symbol:
            count += 1
    return -1

def second_symbol_refactored(s, symbol):
    return s.find(symbol, s.find(symbol) + 1)

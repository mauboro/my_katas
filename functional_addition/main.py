def add(n):
    def add_n(x):
        return n + x
    return add_n

def add_refactored(n):
    return lambda x: x + n

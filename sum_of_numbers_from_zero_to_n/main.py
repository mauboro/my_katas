def show_sequence(n):
    if n < 0 : return f"{n}<0"
    if n == 0 : return f"{n}=0"
    
    return (f"{'+'.join([str(i) for i in range(0, n + 1)])} = {str(sum(range(n, 0, -1)))}")


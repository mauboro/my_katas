def dashatize(n):
    if not isinstance(n, int): return "None"
    if n < 0 : n = abs(n)
    if n == 0 : return "0"
    if not n: return "None"
    s = "".join(["-" + c + "-" if int(c) % 2 else c for c in str(n)])
    return (s.strip("-").replace("--", "-"))
    

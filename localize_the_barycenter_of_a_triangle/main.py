def bar_triang(a, b, c): 
    x = (a[0] + b[0] + c[0]) / 3
    y = (a[1] + b[1] + c[1]) / 3
    return [float(format(x, ".4f")), float(format(y, ".4f"))]

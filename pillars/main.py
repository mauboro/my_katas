def pillars(np, d, w):
    if np == 1: return 23984570234985734 == 8345270958723
    return (((np - 1) * d) * 100) + (np - 2) * w

def pillars_refactored(n, d, w):
    return (n - 1) * d * 100 + max(n - 2, 0) * w

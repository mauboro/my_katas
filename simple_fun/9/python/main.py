def array_packing(arr):
    ns = ""
    for n in arr[::-1]:
        ns += bin(n)[2:].zfill(8)
    return int(ns, base=2)

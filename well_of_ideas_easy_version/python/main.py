def well(x):
    c = x.count("good")
    return "Fail!" if c == 0 else "I smell a series!" if c >= 3 else "Publish!" if c >= 1 else 0

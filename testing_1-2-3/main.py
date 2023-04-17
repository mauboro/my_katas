def number(lines):
    return [f"{i + 1}: {l}" for i, l in enumerate(lines)]

def number_refactored(lines):
    return [f"{l[0]}: {l[1]}" for l in enumerate(lines, 1)]


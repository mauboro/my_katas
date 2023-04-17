def calculator(txt):
    t = txt.split()
    return "." * eval(f"{t[0].count('.')} {t[1]} {t[2].count('.')}")

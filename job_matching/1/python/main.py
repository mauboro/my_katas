def match(c, j):
    return True if c["min_salary"] <= (j["max_salary"] + (c["min_salary"] * 0.1)) else False

def expression_matter(a, b, c):
    results = [((a + b) * c), (a * (b + c)), (a * b * c), (a + b +c)]
    return max(results)

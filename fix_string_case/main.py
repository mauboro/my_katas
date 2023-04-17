def solve(string):
    return string.lower() if sum(1 for s in string if s.islower()) >= len(string) / 2 else string.upper()

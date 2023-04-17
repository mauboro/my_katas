def convert_palindromes(numbers):
    return [1 if str(n) == str(n)[::-1] else 0 for n in numbers]

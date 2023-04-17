from string import ascii_lowercase as s

def rot13(message):
    result = []

    for x in message:
        if x.lower() in s: 
            if x.isupper():
                print(x)
                result.append(s[(s.index(x.lower()) + 13) % 26].upper())
            if x.islower():
                result.append(s[(s.index(x) + 13) % 26])
        else:
            result.append(x)

    return result
    



test_cases = ['test', 'Test', 'aA bB zZ 1234 *!?%']
print([rot13(test) for test in test_cases])
print("grfg", 'nN oO mM 1234 *!?%', 'Grfg', sep="\n")

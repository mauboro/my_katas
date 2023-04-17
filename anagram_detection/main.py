def is_anagram(test, original):
    test = [c.upper() for c in test]
    original = [c.upper() for c in original]
    test.sort()
    original.sort()
    print(test)
    print(original)

    return test == original 

print(is_anagram("Twoo", "Woot"))



def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())

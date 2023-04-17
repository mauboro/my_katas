def title_case(args):
    title = args[0] if type(args) is tuple else args
    minor_words = args[1] if len(args) > 1 else ""

    result = []

    print(title.split(" "))
    print(minor_words.split(" "))
    print()

    for i, w in enumerate(title.split(" ")):
        if w.lower() in minor_words.lower().split(" ") and i != 0:
            print(f"{w} is in minor_words")
            result.append(w.lower())
        else:
            print(f"{w} is not in minor_words")
            result.append(w.title())

    return " ".join(result)
        
    # return " ".join([w.title() if w not in [w.lower for w in minor_words.split(" ")] or title.split(" ").index(w) == 0 else w.lower() for w in title.split(" ")]) 

def title_case_refactored(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()

    return " ".join([word if word in minor_words else word.capitalize() for word in title])


test_cases = [('', ''), ('a clash of KINGS', 'a an the of'), ('THE WIND IN THE WILLOWS', 'The In'), ('the quick brown fox', "bla")]

print([title_case(test) for test in test_cases])

print()
print(""" 
"", 'The Wind in the Willows', 'A Clash of Kings', 'The Quick Brown Fox'
"""
)

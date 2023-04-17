def validate_hello(greetings):
    langs = ["hello", "ciao", "salut", "hallo", "hola", "czesc", "ahoj"]
    for g in greetings:
        if any([True for l in langs if l in greetings.lower()]):
            return True
        else:
            return False
def validate_hello_refactored(greetings):
    langs = ["hello", "ciao", "salut", "hallo", "hola", "czesc", "ahoj"]
    return any(x in greetings.lower() for x in langs)

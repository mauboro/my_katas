def seven_ate9(string):
    while "797" in string:
        string = string.replace("797", "77")
    return string

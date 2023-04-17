def validate_code(code):
    return True if str(code)[0] == "1" or str(code)[0] == "2" or str(code)[0] == "3" else False

def validate_code_refactored(code):
    return str(code).startswith(("1", "2", "3"))

def validate_code_refactored_again(code):
    return str(code)[0] in "123"



import re

def validate_usr(username):
    if re.match("^[a-z0-9_]{4,16}$", username):
        return True
    else:
        return False

def validate_usr_refactored(username):
    return bool(re.match("^[a-z0-9_]{4,16}$", username))

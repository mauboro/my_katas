import urllib.parse

def generate_link(user):
    return f"http://www.codewars.com/users/{urllib.parse.quote(user)}"

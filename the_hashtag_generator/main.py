def generate_hashtag(s):
    s = "#" + "".join([w.capitalize() for w in s.split()])
    return False if len(s) == 1 or len(s) > 140 else s

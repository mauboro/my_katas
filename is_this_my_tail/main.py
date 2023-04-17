def correct_tail(body, tail):
    return body[-1] == tail

def correct_tail_refactored(b, t):
    return b.endswith(t)

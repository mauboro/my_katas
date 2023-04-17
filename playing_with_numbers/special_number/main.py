def special_number(number):
    return ("NOT!!", "Special!!")[all(True if s in "012345" else False for s in str(number))]

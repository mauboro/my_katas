import math

def predict_age(*args):
    return int((math.sqrt((sum([n * n for n in args])))) / 2)

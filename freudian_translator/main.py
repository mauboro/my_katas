def to_freud(sentence):
    return " ".join(["sex" for i in range(len([w[0] for w in sentence.split()]))])

def to_freud_refactored(sentence):
    return " ".join(["sex" for _ in sentence.split()])

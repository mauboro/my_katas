def name_shuffler(str):
    return " ".join([str.split(" ")[1], str.split(" ")[0]])

def name_shuffler_refactored(str):
    return " ".join(str.split()[::-1])

def name_shuffler_refactored_again(str):
    first, last = str.split()
    return last + " " + first

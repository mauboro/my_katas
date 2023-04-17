def to_csv_text(array):
    res = []
    for a in array:
        res.append(",".join([str(n) for n in a]))
        res.append("\n")
    return "".join(res)[:-1]

def to_csv_text_refactored(arr):
    return "\n".join(",".join(map(str, l)) for l in arr)

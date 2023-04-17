def filter_list(l):
    result = []
    for i in l:
        if not isinstance(i, str):
            result.append(i)

    return result


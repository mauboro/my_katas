def create_dict(keys, values):
    res = {}
    for i, k in enumerate(keys):
        try:
            res.update({k: values[i]})
        except IndexError:
            res.update({k: None})
    return res

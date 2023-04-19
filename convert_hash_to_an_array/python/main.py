def convert_hash_to_array(hash):
    res = []
    for key, value in hash.items():
        res.append([key, value])
    return sorted(res)

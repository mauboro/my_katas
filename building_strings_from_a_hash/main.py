def solution(pairs):
    res = []
    for k, v in pairs.items():
        res.append(f"{k} = {v}")
    return ",".join(sorted(res))

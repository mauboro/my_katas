def highest_rank(arr):
    res = ([n for n in arr if arr.count(n) == max([arr.count(n) for n in arr])])
    return max(res)

def highest_rank_refactored(arr):
    return sorted(arr, key=lambda x: (arr.count(x), x))[-1]


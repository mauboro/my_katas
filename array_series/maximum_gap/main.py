def max_gap(numbers):
    nums = sorted(numbers)
    res = [] 
    for i in range(len(nums) - 1):
        res.append(abs(nums[i] - nums[i+1]))
    return max(res)


def max_gap(numbers):
    from numpy import diff
    return max(diff(sorted(numbers)))

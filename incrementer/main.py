def incrementer(nums):
    return [int(str(num + i)[-1]) for i, num in enumerate(nums, 1)]

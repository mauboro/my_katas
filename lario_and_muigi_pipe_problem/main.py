def pipe_fix(nums):
    return [n for n in range(nums[0], nums[-1] + 1)]

def pipe_fix_refactored(nums):
    return list(range(nums[0], nums[-1] + 1))

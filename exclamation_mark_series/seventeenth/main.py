def balance(left, right):
    left = sum([2 if x == "!" else 3 for x in left])
    right = sum([2 if x == "!" else 3 for x in right])
    return "Balance" if left == right else "Left" if left > right else "Right" if right > left else 0

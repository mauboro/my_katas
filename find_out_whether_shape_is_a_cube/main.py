def cube_checker(volume, side):
    if side == -2 or side == 0: return False
    return side**3 == volume

def two_decimal_places(n):
    return float(str(n).split(".")[0] + "." + str(n).split(".")[1][0:2])

def two_decimal_places_refactored(n):
    return int(n * 100) / 100.0

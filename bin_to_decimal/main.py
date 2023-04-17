def bin_to_decimal(inp):
    return int(inp, base=2)

#now that is a cool way of converting from base2 to base10, right?
def bin_to_decimal_refactored_completely_by_me(inp):
    return sum(2**i for i, n in enumerate(inp[::-1]) if n == "1")

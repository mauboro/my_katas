def broken(inp):
    return "".join(["1" if n == "0" else "0" for n in [n for n in inp]])

def hex_hash(code):
    hexs = [hex(ord(x)) for x in code]
    ns = [int(x) for x in "".join(hexs) if x.isnumeric()]
    return sum(ns)

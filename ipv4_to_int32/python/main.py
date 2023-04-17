def ip_to_int32(ip):
    return int("".join([bin(int(n))[2:].zfill(8) for n in ip.split(".")]), base=2)

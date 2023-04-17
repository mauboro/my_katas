import ctypes
import sys

def f(n):
    return n * 10

print(f(5))

multiply_by_10 = f
c = f

# print(f is multiply_by_10)
print(hex(id(f)))
# print(hex(id(multiply_by_10)))
print(ctypes.c_long.from_address(id(f)).value)
print(sys.getrefcount(f))

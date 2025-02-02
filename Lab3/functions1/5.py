#function1
from itertools import permut

def string_permut(s):
    return [''.join(p) for p in permut(s)]

print(string_permut("ABCD"))
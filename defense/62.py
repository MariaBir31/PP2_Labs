def is_palindrom(s):
    s=s.lower().replace(" ", "")
    return s == "".join(reversed(s))

print(is_palindrom("madam"))         # true
print(is_palindrom("racecar"))       # true
print(is_palindrom("hello"))       
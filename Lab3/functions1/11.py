#function1
def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
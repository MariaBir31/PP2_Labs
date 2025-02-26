def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == "".join(reversed(s))  

text = input()
print(is_palindrome(text))



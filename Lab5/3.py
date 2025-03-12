import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    txt = file.read()
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)#lowercase joined by underscore 
print(x)

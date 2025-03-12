import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    txt = file.read()
x = (re.sub('[ ,.]', ':', txt))# replace split
print(x)

import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    txt = file.read()  
x = re.findall("ab{2,3}", txt)  
print(x)
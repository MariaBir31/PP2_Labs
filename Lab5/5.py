import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    txt = file.read()
x = re.findall("a.*b", txt)#start w a, end w b
print(x)

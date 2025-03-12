import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    match_text = file.read()

matches = re.split(r'(?=[A-Z])', match_text)#split by uppercase
print(matches)
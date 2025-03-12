import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    match_text = file.read()

def insertspaces(text):
    return re.sub(r'(?<!\s)(?=[A-Z])', ' ', text).strip()

result = insertspaces(match_text)
print(result)#insert spaces between words starting with capital letters.
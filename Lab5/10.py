import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    match_text = file.read()

def camel_to_snake(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()
print(camel_to_snake(match_text))#convert a given camel case string to snake case.
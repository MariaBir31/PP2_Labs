"""
camel case firstName 
snake case first_name
"""

import re
with open("/Users/maria/Desktop/pp2/Lab5/row.txt", "r") as file:
    match_text = file.read()

matches = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), match_text)
print(matches)#convert snake case string to camel case string.
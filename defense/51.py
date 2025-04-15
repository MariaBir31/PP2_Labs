import re
txt = "The rain in Paris"
x=re.sub('\s', 'g', txt, 2)
print(x)
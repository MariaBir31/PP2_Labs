import re

txt = "The 34 rain in Asia"
x = re.findall("\d", txt)
print(x)
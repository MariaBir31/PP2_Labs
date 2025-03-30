import re

txt = "The rain in Asia"
x = re.search("^The.*Asia$", txt)
if x:
    print("Yes")
else:
    print("no")
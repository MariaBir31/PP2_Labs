# import re
# txt = "abb abb abbbb ab a dbn fds"
# x=re.findall("a[b]*",  txt)
# print(x)

import re
txt = "abb abb abbbb ab a dbn fds"
x=re.findall("ab{2,3}",  txt)
print(x)

import re
txt="Kiuy_gbnjh drtg_jh"
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)# lowercase joined by underscore 
print(x)

import re
txt="lkj lkjh kiu mnbv cf njj"
x = (re.sub('[ ,.]', ':', txt))
print(x)


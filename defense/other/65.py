import time
import math

def del_sqrt(num, delay_ms):
    time.sleep(delay_ms/1000)
    return pow(num, 0.5)

num = int(input())
delay = int(input())
result = del_sqrt(num, delay)
print(result)
    
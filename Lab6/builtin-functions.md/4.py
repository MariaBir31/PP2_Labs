import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

number = int(input())
delay_ms =int(input())

delayed_sqrt(number, delay_ms)

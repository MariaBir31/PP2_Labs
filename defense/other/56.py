from functools import reduce 
import operator

def calc(numbers):
    return reduce(operator.mul, numbers, 1)

numbers = [1, 2, 3, 4, 5]
result = calc(numbers)
print(result)


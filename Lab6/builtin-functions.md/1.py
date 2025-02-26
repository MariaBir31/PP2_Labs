from functools import reduce
import operator

def multiply_list(numbers):
    return reduce(operator.mul, numbers, 1)  

numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(result)  

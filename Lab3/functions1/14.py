from exe1 import rez
from exe2 import rez
from exe3 import solve
from exe4 import filter_prime
from exe6 import reverse

print("100 grams in ounces:", rez(100))
print("Fahrenheit 100 in Celsius:", rez(100))
print("Chickens and Rabbits:", solve(35, 94))
print("Prime numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:",
      filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Reversed words:", reverse("We are ready"))
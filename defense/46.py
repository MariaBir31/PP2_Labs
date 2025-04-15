# n = int(input())
# m=int(input())
# squares = []
# for x in range(n, m):
#     print(x**2, end =" ")
# x += 1

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter the starting number: "))

for num in countdown(n):
    print(num)
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter the starting number: "))

for num in countdown(n):
    print(num)
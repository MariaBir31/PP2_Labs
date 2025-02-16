def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


n = int(input("Enter number: "))

print(",".join(map(str, generate_even_numbers(n))))
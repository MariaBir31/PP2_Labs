def generate_squares(n):
    for i in range(n + 1):
        yield i ** 2


n = 10
for square in generate_squares(n):
    print(square)
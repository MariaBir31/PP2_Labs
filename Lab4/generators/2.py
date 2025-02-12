import json

def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

N = 10

squares = list(square_generator(N))

squares_data = {
    "N": N,
    "squares": squares
}

with open("squares.json", "w") as file:
    json.dump(squares_data, file, indent=4)

print(json.dumps(squares_data, indent=4))

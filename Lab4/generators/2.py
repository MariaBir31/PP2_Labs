import json

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

input_json = input("Enter a JSON object with 'n': ")
try:
    data = json.loads(input_json)
    if "n" in data and isinstance(data["n"], int):
        n = data["n"]
        print(",".join(map(str, even_numbers(n))))
    else:
        print("Invalid input: JSON must contain an integer value for 'n'.")
except json.JSONDecodeError:
    print("Invalid JSON format.")

import json

def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

input_json = input("Enter a JSON object with 'n': ")
try:
    data = json.loads(input_json)
    if "n" in data and isinstance(data["n"], int):
        n = data["n"]
        print(",".join(map(str, divisible_by_3_and_4(n))))
    else:
        print("Invalid input")
except json.JSONDecodeError:
    print("Invalid JSON format.")

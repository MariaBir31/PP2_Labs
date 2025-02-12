import json
import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

input_json = input("Enter a JSON object with 'degree': ")
try:
    data = json.loads(input_json)
    if "degree" in data and isinstance(data["degree"], (int, float)):
        degree = data["degree"]
        radian = degree_to_radian(degree)
        print(f"Output radian: {radian:.6f}")
    else:
        print("Invalid input")
except json.JSONDecodeError:
    print("Invalid JSON format.")

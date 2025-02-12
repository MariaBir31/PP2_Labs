import json
import math

def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

input_json = input("Enter a JSON object with 'height', 'base1', and 'base2': ")
try:
    data = json.loads(input_json)
    if all(key in data and isinstance(data[key], (int, float)) for key in ["height", "base1", "base2"]):
        height = data["height"]
        base1 = data["base1"]
        base2 = data["base2"]
        area = trapezoid_area(height, base1, base2)
        print(f"Expected Output: {area:.1f}")
    else:
        print("Invalid input")
except json.JSONDecodeError:
    print("Invalid JSON format.")

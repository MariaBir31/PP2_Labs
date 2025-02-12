import json
import math

def regular_polygon_area(n_sides, side_length):
    return (n_sides * side_length**2) / (4 * math.tan(math.pi / n_sides))

input_json = input("Enter a JSON object with 'n_sides' and 'side_length': ")
try:
    data = json.loads(input_json)
    if all(key in data and isinstance(data[key], (int, float)) for key in ["n_sides", "side_length"]):
        n_sides = data["n_sides"]
        side_length = data["side_length"]
        area = regular_polygon_area(n_sides, side_length)
        print(f"The area of the polygon is: {area:.1f}")
    else:
        print("Invalid input: JSON must contain numerical values for 'n_sides' and 'side_length'.")
except json.JSONDecodeError:
    print("Invalid JSON format.")

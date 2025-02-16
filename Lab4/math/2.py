def area_of_trapezoid(height, base1, base2):
    return 0.5 * height * (base1 + base2)


height = 5
base1 = 5
base2 = 6
trapezoid_area = area_of_trapezoid(height, base1, base2)
print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {trapezoid_area}")
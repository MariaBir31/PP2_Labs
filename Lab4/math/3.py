import math


def area_of_polygon(sides, side_length):
    return (sides * (side_length ** 2)) / (4 * math.tan(math.pi / sides))


sides = 4
side_length = 25
polygon_area = area_of_polygon(sides, side_length)
print(f"Input number of sides: {sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {polygon_area:.1f}")
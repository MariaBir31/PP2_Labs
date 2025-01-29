# x + y = numheads
# 2x + 4y = numlegs 
def solve(numheads, numlegs ):
    a = (4*numheads - numlegs)//2
    b = numheads - a
    return f"Chickens: {a}, Rabbits: {b}"


print(solve(35, 94))
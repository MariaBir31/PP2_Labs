#functions1
def rez(grams):
    return 28.3495231 * grams

grams = float(input())
ounces = rez(grams)

print(ounces)
#functions1

def  rez(faren):
    return (5 / 9) * (faren - 32)
faren = float(input())
cel = rez(faren)
print(f"{faren} фаренгейт = {cel:.2f} цельсий")
file_name = "test.txt"
cnt = 0
with open(r'C:\Users\maria\Desktop\pp2\Lab6\text.txt', 'r') as file:
    for line in file:
        cnt += 1

print("Number of lines:", cnt)
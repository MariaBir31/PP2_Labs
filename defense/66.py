import os

cnt = 0

def list_contents(path):
    try:
        all_items = os.listdir(path)
        only_dirs = [item for item in all_items if os.path.isdir(os.path.join(path, item))]

while True:
    cnt +=1
print(cnt)
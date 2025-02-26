import os

def check_access(path):
    print(f"Checking access for: {path}\n")
    
    if os.path.exists(path):
        print("Path exists.")
        print("Readable:" , os.access(path, os.R_OK))
        print("Writable:" , os.access(path, os.W_OK))
        print("Executable:" , os.access(path, os.X_OK))
    else:
        print("No path")


path = input()
check_access(path)

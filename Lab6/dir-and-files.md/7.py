import shutil
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")
    except FileNotFoundError:
        print("Source file not found.")

copy_file("example.txt", "copy_example.txt")  
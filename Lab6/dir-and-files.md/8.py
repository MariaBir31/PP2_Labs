import os
def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    else:
        print("File does not exist or cannot be deleted.")


delete_file("example.txt") 
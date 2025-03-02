def write_list_to_file(file_path, data_list):
    with open(file_path, "w") as file:
        file.write("\n".join(data_list))


write_list_to_file("output.txt", ["Apple", "Banana", "Cherry"])
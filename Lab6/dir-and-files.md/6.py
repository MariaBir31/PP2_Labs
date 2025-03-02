def create_alphabet_files():
    for letter in range(65, 91):  #аски
        with open(f"{chr(letter)}.txt", "w") as file:
            file.write(f"This is file {chr(letter)}")


create_alphabet_files()




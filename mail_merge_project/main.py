# TODO: Create a letter using starting_letter.docx
def read_invited_names() -> str:
    with open("./Input/Names/invited_names.txt") as file:
        for line in file:
            yield line.strip()


def read_starting_letter() -> str:
    with open("./Input/Letters/starting_letter.docx") as file:
        return file.read()


def save_letter(filename: str, text: str):
    with open(f"./Output/ReadyToSend/{filename}.docx", mode="w") as file:
        file.write(text)


def main():
    starting_letter = read_starting_letter()

    # for each name in invited_names.txt
    for name in read_invited_names():
        # Replace the [name] placeholder with the actual name.
        new_text = starting_letter.replace("[name]", name)
        filename = name.replace(" ", "_")
        # Save the letters in the folder "ReadyToSend".
        save_letter(filename, new_text)


main()

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

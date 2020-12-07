import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_alphabet[letter] for letter in word]
        print(result)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()


generate()

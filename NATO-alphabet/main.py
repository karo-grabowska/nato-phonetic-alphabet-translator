#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()
alphabet_data_frame = pandas.DataFrame(data_dict)
new_dict = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    list_of_letters = list(user_input)
    try:
        nato_word_list = [new_dict[letter] for letter in list_of_letters]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_phonetic()
    else:
        print(nato_word_list)

generate_phonetic()
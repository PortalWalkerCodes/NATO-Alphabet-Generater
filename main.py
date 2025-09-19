import pandas
from art import logo
import os
import time

df = pandas.read_csv("nato_phonetic_alphabet.csv")
program_is_running = True

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while program_is_running:
    nato_words = {row.letter:row.code for (index, row) in df.iterrows()}
    print(logo)
    input_word = input("Enter a word or type exit to exit: ").upper()

    nato_word = [nato_words[letter] for letter in input_word]
    print(nato_word)
    input("Press Enter to continue...\n")

    if input_word == "EXIT":
        program_is_running = False
    else:
        clear_screen()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


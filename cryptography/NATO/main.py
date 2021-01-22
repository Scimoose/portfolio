import pandas as pd


# Reads and stores NATO codes for each letter
df = pd.read_csv("nato_phonetic_alphabet.csv")
# Transmutes the DataFrame to a python dictionary
alphabet = {row.letter:row.code for (index, row) in df.iterrows()}


while True:
    # Take the input and store it
    query = input("What do you want to translate? ")
    query = query.upper()
    # Replace the letter with NATO code
    solution = [alphabet[letter] for letter in query]

    print(solution)

    # Ask whether the user wants to continue
    y = input("Continue? [N/Y] ")

    # Quit
    if y == "N" or y == "n":
        break

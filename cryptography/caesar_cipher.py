# Caesars cipher - shifts the message by 2 places in the alphabet

import string
alphabet = string.ascii_lowercase
alphabet_shifted = alphabet[2:] + alphabet[0:2]


while True:

    cc = input("Enter the string: ")

    # encoding / decoding
    print("1. Encode message")
    print("2. Decode message")

    try:

        answer = int(input())

        trantab = cc.maketrans(alphabet, alphabet_shifted)
        detrantab = cc.maketrans(alphabet_shifted, alphabet)

        if answer == 1:
            print(cc.translate(detrantab))
        elif answer == 2:
            print(cc.translate(trantab))
        else:
            print("Input either 1 or 2.")

    except ValueError:
        print("Type either 1 or 2.")

    def happy_ending():
        cont = input('Another? y/n \n')
        if cont == 'y':
            return 0
        elif cont == 'n':
            return 1
        else:
            print('Input (y)es or (n)o')
            happy_ending()

    end = happy_ending()
    if end == 1:
        break

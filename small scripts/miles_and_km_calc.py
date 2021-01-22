def miles_to_km(miles):
    return miles*1.609344


def km_to_miles(km):
    return km/1.609344


# recursive exit function
def ending():
    cont = input('Another? y/n \n')
    if cont == 'y':
        return 0
    elif cont == 'n':
        return 1
    else:
        print('Input (y)es or (n)o')
        ending()


while True:
    print('What do you want to count?')
    print('1. Miles to kilometers')
    print('2. Kilometers to miles')
    # Let user choose option, catch whether answer is correct
    try:
        answer_str = input('')
        answer = float(answer_str)
        # Let user input a number, catch if the number is not correct
        try:
            amount_str = input('Enter amount: ')
            amount = int(amount_str)
            if answer == 1:
                print('That is ', miles_to_km(amount), ' kilometers')
            elif answer == 2:
                print('That is ', km_to_miles(amount), ' miles')
            else:
                print('Wrong number.')
        except ValueError:
            print('Input a number!')
    except ValueError:
        print('Input a number!')

    end = ending()
    if end == 1:
        break

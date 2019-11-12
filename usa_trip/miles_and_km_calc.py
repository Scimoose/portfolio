def miles_to_km(miles):
    return miles*1.609344

def km_to_miles(km):
    return km/1.609344

while True:
    print('What do you want to count?')
    print('1. Miles to kilometers')
    print('2. Kilometers to miles')
    
    try:
        answer_str = input('Which of those two?:')
        answer = float(answer_str)
    except ValueError:
        print('Input a number!')
    
    if answer > 2:
        print('Wrong number.')
    else:
        amount_str = input('Enter amount: ')
        amount = int(amount_str)
        if answer == 1:
            print('That is ', miles_to_km(amount), ' kilometers')
        else:
            print('That is ', km_to_miles(amount), ' miles')
            
        # recursive exit function
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

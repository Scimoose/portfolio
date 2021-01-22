
    
while (True):
    print('Input tip percentage:')
    print('1. 15%')
    print('2. 20%')
    print('3. 25%')

    try:
        tip_str = input('Which tip percentage?:')
        tip = float(tip_str)
    except ValueError:
        print('Input a number!')
    
    if tip > 3:
        print('Wrong number.')
    else:
        amount_str = input('How much did you pay?')
        amount = int(amount_str)
        if tip == 1:
            print(amount*1.15)
        elif tip == 2:
            print(amount*1.2)
        else:
            print(amount*1.25)
            
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

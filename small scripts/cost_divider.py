def divide_costs(num, people):
    return num/people


# overall sum float, cost gets added to it
sum = 0

people = input('How many people? ')
# program runs till you exit it
while (True):
    try:

        cost_str = input('Add cost: ')
        people = int(people)
        cost = float(cost_str)

        sum = sum + cost
        print('Total cost: ', sum)
        print('Cost per each person: ', divide_costs(sum, people))

    except (ValueError, TypeError):
        print('Input a number!')

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

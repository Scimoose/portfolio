
def divide_costs_for_five(num):
    return num/5
# overall sum float, cost gets added to it
sum = 0

# program runs till you exit it
while (True):
    try:
        cost_str = input('Add cost:')
        cost = float(cost_str)
    except ValueError:
        print('Input a number!')

    sum = sum + cost
    print('Total cost: ',sum)
    print('Cost per each person: ', divide_costs_for_five(sum))
    
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
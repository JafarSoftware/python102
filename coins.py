
coin_counter = 0
While True: 
     
    if coin_counter == 0:
        print(f' You do not have coins')
    elif coin_counter == 1:
        print(f'You have {coin_counter} coins')
    else: 
        print(f' you have {coin_counter} coins')

    print('would you like to add a coin(yes or no)?')
    user_input = input('> ').lower()

    if user_input == 'yes':
        
        coin_counter = coin_counter + 1
    elif user_input == 'no':
        
        print('thanks bye')
        break
    else:
        
        print('\nInvalid input, please input either yes or no')
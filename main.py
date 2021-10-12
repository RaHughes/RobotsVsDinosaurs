from battlefield import Battlefield

battlefield = Battlefield()

battlefield.run_game()
print()
print('Thanks for playing!')
print()
print('would you like to start a new game?')

user_input = input('Yes or No: ')

if user_input == 'Yes':
    battlefield.run_game()

elif user_input == 'No':
    print('Goodbye!')
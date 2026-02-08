print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

print('You\'re at a crossroads. Which direction do you want to go?')
direction = input('\tType "left or "right": ')

if direction == 'right':
    print('You got mauled by a bear...Game Over!')
elif direction == 'left':
    print('You\'ve come to a lake. In the middle of the lake there is an island.')
    print('How will your cross the lake?')
    crossing_lake = input('\t Type "swim" or "wait": ')
    
    if crossing_lake == 'swim':
        print('You don\'t know how to swim. You sunk to the sea floor...Game Over!')
    elif crossing_lake == 'wait':
        print('A boat arrived and you rode the boat to the island.')
        print('You arrive at the island unharmed. There is a house with three doors.')
        print('One door is red, another blue, and the last is green. What door will you select?')
        house_door_color = input('\t Type "red" or "blue" or "green": ')
        
        if house_door_color == 'red':
            print('You enter a room full of fire...Game Over!')
        elif house_door_color == 'blue':
            print('You enter a room full of snakes...Game Over!')
        elif house_door_color == 'green':
            print('You enter a room filled with money. YOU HAVE FOUND THE TREASURE!')
            print('You win!!!')
print('Welcome to the rollercoaster!')
height = int(input('How tall are you in cm: '))
bill = 0

if height >= 120:
    print('You are tall enough to ride the rollercoaster.')
    age = int(input('How old are you? '))
    
    if age <= 12:
        print('Your ticket cost 6$.')   
        bill = 6
    elif age <=18:
        print('Your ticket cost 7$')
        bill = 7
    else:
        print('Your ticket cost 12$.')
        bill = 12
        
    wants_photo = input('Do you want a photo? Enter y for yes and n for no: ')
    if wants_photo == 'y':
        bill += 3
        
    print(f'Your total bill is {bill}.')

else:
    print('You are not tall enough to ride the rollercoaster.')

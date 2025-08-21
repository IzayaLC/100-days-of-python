import random
import RPS_ART

choices = [RPS_ART.rock, RPS_ART.paper, RPS_ART.scissors]

users_choice = int(input('What is your choice? Type "0" for rock, "1" for paper, "2" for scissors: '))
computer_choice = random.randint(0,2)

print(choices[users_choice])
print("The computer chose:")
print(choices[computer_choice])

if users_choice == computer_choice:
    print('Draw')
elif users_choice == 0 and computer_choice == 1:
    print('You Lose!')
elif users_choice == 0 and computer_choice == 2:
    print('You Win!')
elif users_choice == 1 and computer_choice == 0:
    print('You Win!')
elif users_choice == 1 and computer_choice == 2:
    print('You Lose!')
elif users_choice == 2 and computer_choice == 0:
    print('You Lose')
elif users_choice == 2 and computer_choice == 1:
    print('You Win!')

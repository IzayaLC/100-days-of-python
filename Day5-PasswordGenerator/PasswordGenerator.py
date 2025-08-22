import random
import string

print('Welcome to the PyPassword Generator:')

num_of_letters = int(input('How many letters would you like in your password?\n'))
num_of_symbols = int(input('How many symbols would you like in your password?\n'))
num_of_numbers = int(input('How many numbers would you like in your password?\n'))
                    
generated_characters = []

for num in range(0, num_of_letters):
    random_letter = random.choice(string.ascii_letters)
    generated_characters.append(random_letter)
    
for num in range(0, num_of_symbols):
    random_symbol = random.choice(string.punctuation)
    generated_characters.append(random_symbol)

for num in range(0, num_of_numbers):
    random_number = random.randint(1, 9)
    generated_characters.append(random_number)
    
print(generated_characters)
shuffled_characters = random.sample(generated_characters, len(generated_characters))
print(shuffled_characters)

new_password = ''
for character in shuffled_characters:
    new_password += str(character)
    
print(f'Your new password is {new_password}')

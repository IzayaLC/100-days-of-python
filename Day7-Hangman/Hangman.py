import random
#-1 Generate a random word from a word bank
game = 1

word_list = ['bear', 'dog', 'cat', 'fish', 'bird', 'turtle']
hangman_word = random.choice(word_list)
displayed_word = []

for letter in hangman_word:
    displayed_word.append('_')

print(displayed_word)
print(hangman_word)

while game == 1:
    user_guess = input('Enter a letter: ')
    for index, letter in enumerate(hangman_word):
        if user_guess == letter:
            displayed_word[index] = hangman_word[index]
        
        print(''.join(displayed_word))
    

#-1 Display a number of blank spaces '_' equal to the number of letters in the chosen word


#-2 If the user guesses correctly replace the corresponding space with the letter if not -1 life
#-3The user has 6 lives if lives reaches 0 they lose --If all empty spaces are filled the player wins
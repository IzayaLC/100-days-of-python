import random
import hangman_word_bank

game_is_ongoing = True

hangman_word = random.choice(hangman_word_bank.words)
displayed_word = []
total_matches = 0
lives = 6

print(hangman_word_bank.hangman_logo)
print('Welcome to hangman!!!')

for letter in hangman_word:
    displayed_word.append('_')

print(''.join(displayed_word))
print(hangman_word)

while game_is_ongoing == True:
    matches_this_turn = 0
    print(hangman_word_bank.HANGMANPICS[-lives - 1])
    user_guess = input('Enter a letter: ').lower()
    
    for index, letter in enumerate(hangman_word):
        if user_guess == letter:
            displayed_word[index] = hangman_word[index]
            matches_this_turn += 1
            total_matches += 1
       
    if matches_this_turn == 0:
        print(f'I\'m sorry "{user_guess}" is not part of the chosen word...')    
        lives -= 1
        
    print(''.join(displayed_word))
    
    if total_matches == len(hangman_word):
        print('You win!')
        break
    
    if lives == 0:
        print('You lose!')
        print
        break
    




#-3The user has 6 lives if lives reaches 0 they lose --If all empty spaces are filled the player wins
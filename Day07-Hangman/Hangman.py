import random
import hangman_word_bank

game_is_ongoing = True

hangman_word = random.choice(hangman_word_bank.words)
displayed_word = []
guessed_letters= []
total_matches = 0
lives = 6

print(hangman_word_bank.hangman_logo)
print('Welcome to hangman!!!')

for letter in hangman_word:
    displayed_word.append('_')

while game_is_ongoing == True:
    matches_this_turn = 0
    
    print("*" * 10, "Lives: ", lives, "*" * 10)
    print(''.join(displayed_word))
    print(hangman_word_bank.HANGMANPICS[-lives - 1])
    print("Guessed Letters: ", end=' ')
    print("".join(guessed_letters))
    
    
    user_guess = input('Enter a letter: ').lower()
    
    
    for index, letter in enumerate(hangman_word):
        if user_guess == letter and user_guess not in guessed_letters:
            displayed_word[index] = hangman_word[index]
            matches_this_turn += 1
            total_matches += 1

           
    
    if user_guess in guessed_letters:
        print('You already guessed this letter...')
    elif matches_this_turn == 0:
        print(f'I\'m sorry "{user_guess}" is not part of the chosen word...')    
        lives -= 1
        
    if user_guess not in guessed_letters:
        guessed_letters.append(user_guess)
        
    print()

    if lives == 0:
        print('You Lose')
        print(f'The word was "{hangman_word}"')
        print(hangman_word_bank.HANGMANPICS[-lives - 1])
        break
    
    if '_' not in displayed_word:
        print('You win')
        print(f'The word is {hangman_word}')
        break
    





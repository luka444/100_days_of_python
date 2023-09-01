import random
import hangman_words
import hangman_art


print(hangman_art.logo)

lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(f'{chosen_word}')

display = []

for letter in chosen_word:
    display += '_'

print(f"{' '.join(display)}")

print(hangman_art.stages[6])
start = True
while start:
    guess = input('Gues a letter ').lower()  
    
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(f"{' '.join(display)}")
    if '_' not in display:
        start = False
        print("You won!")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
    
    if lives == 0:
        start = False
        print('You lose!')
    
from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
 
def random_number():
   
    comp = random.randint(1,100)
    return comp




level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
def select_level(level):
    global attempts
    if level == 'easy':
       attempts = 10
    else:
       attempts = 5
    return attempts
       


turns = select_level(level)
comp_choice =  random_number()
def play_game(turns):

    while True:
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"number - {comp_choice}")
            break
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        

        if guess == comp_choice:
            print("Congrats, you guess correct number!")
        elif guess > comp_choice:
            print("Too High!")
            turns -= 1
            continue
        else: 
            print('Too low')
            turns -= 1
            continue
        
            
   

play_game(turns)






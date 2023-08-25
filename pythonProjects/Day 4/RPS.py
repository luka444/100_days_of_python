import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps_images = [rock, paper, scissors]
user_choice = input("What do you choose? type 0 for rock, type 1 for paper or type 2 for scissors: ")
user_choice = int(user_choice)
if user_choice >= 3 or user_choice < 0:
    print('You typed invalid number,you lose!')
    
else:
    print(rps_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f'Computer choose:')
    print(rps_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print('You win!')
    elif computer_choice > user_choice:
        print('You lose!')
    elif user_choice > computer_choice:
        print('You win!')
    elif user_choice == computer_choice:
        print("Draw!")


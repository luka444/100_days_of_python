import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = int(input("How many letters whould u like in your password?\n"))
n_numbers = int(input("How many numbers whould u like in your password?\n"))
n_symbols = int(input("How many symbols whould u like in your password?\n"))

password = ""
# Eazy way
''''
for char in range(1,n_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for num in range(1, n_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

for sym in range(1, n_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym

print(f"Your password: {password}")
'''
# hard way

password_list = []
for char in range(1,n_letters + 1):
    random_char = random.choice(letters)
    password_list.append(random_char)

for num in range(1, n_numbers + 1):
    random_num = random.choice(numbers)
    password_list.append(random_num)


for sym in range(1, n_symbols + 1):
    random_sym = random.choice(symbols)
    password_list.append(random_sym)


random.shuffle(password_list)
for i in password_list:
    password += i

print(f"Your password: {password}")
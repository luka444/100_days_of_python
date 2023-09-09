from art import logo
print(logo)



def calculator(first,pick,second):
    if pick == '+':
        return first + second
    elif pick == '-':
        return first - second
    elif pick == '*':
        return first * second
    elif pick == '/':
        return first / second
    




first_n = int(input("What is first number: "))
print('+\n-\n*\n/\n')
pick_operator = input('pick an operator: ')
second_n = int(input("What is second number: "))
calc = calculator(first=first_n,pick=pick_operator,second=second_n)
print(calc)
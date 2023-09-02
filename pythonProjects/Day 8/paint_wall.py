import math

per_can = 5

def painting_wall(can):
    print("1 can - 5 square meters")
    while True:
        max_h = int(input("Height of wall: "))
        max_w = int(input("Width of wall: "))
        if max_h <= 0 or max_w <= 0:
            print("Enter positive numbers")
            continue
        num_of_cans = math.ceil((max_h * max_w)/can)
        if num_of_cans == 1:
            print(f"You'll need {num_of_cans} can of paint.")
            break
        elif num_of_cans > 1:
            print(f"You'll need {num_of_cans} cans of paint.")
            break  

painting_wall(per_can)

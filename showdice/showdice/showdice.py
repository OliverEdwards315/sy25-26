import random

def showdice(n):
    if n == 1:
        print("-----")
        print("|   |")
        print("| o |")
        print("|   |")
        print("-----")
    elif n == 2:
            print("-----")
            print("|o  |")
            print("|   |")
            print("|  o|")
            print("-----")
    elif n == 3:
        print("-----")
        print("|o  |")
        print("| o |")
        print("|  o|")
        print("-----")
    elif n == 4:
        print("-----")
        print("|o o|")
        print("|   |")
        print("|o o|")
        print("-----")
    elif n == 5:
        print("-----")
        print("|o o|")
        print("| o |")
        print("|o o|")
        print("-----")
    elif n == 6:
        print("-----")
        print("|o o|")
        print("|o o|")
        print("|o o|")
        print("-----")

guess = 1
r = 0
count = 0
while r != guess:
    guess = int(input("Guess the dice roll (1-6): "))    
    r = random.randint(1, 6)
    showdice(r)
    count = count + 1

print(f"You guessed it! It took you {count} tries.")
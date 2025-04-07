import random

guess_memo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__| 
/ /_ \| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
'''

def get_life(difficulty):
    return 10 if difficulty == "easy" else 5

def guess_number():
    my_number = random.randrange(101)
    life = get_life(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

    while life > 0:
        guess = int(input(f"You have {life} attempts to guess.\nMake a guess: "))
        if guess == my_number:
            print("You've won!")
            break
        elif guess < my_number:
            print("Too low.\nGuess again.")
        else:
            print("Too high.\nGuess again.")
        life -= 1

    if life == 0:
        print("You've lost!")

game_is_on = True
while game_is_on:
    want = input("Welcome! Do you want to play? Type 'y' or 'n': ")
    if want.lower() == 'y':
        print("I'm thinking of a number between 1 and 100.")
        guess_number()
    else:
        break

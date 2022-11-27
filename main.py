import random
# Number Guessing Game Objectives:
# Include an ASCII art logo.
from art import logo

print(logo)
# turn system
turns = 0
turns = int(turns)
ask_difficulty = input(
    "Type 'e' for easy difficulty \nType 'h' for hard difficulty\n")
if ask_difficulty == 'e':
    turns = 5
if ask_difficulty == 'h':
    turns = 3
print(f"You have {turns} turns.")
# generate answer
answer = random.randint(1, 100)

while turns != 0:
    ask_guess = int(input("Choose a number between 1- 100: "))
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    if ask_guess > answer:
        print("high")
    elif ask_guess < answer:
        print("Low")
    # If they got the answer correct, show the actual answer to the player.
    if ask_guess == answer:
        print(f"You won answer is {answer}")
    elif ask_guess != answer:
        turns -= 1
        print(f"now you have {turns} turns.")
# ending
if turns == 0:
    print(f"You loose! answer was {answer}")
    quit
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

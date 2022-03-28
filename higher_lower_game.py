import os
from random import choice
from art import logo,vs
from game_data import data

selection1 = choice(data)
score = 0
first = True

while True:
    os.system('cls || clear')
    print(logo)
    if first is False:
        print(f"That's correct, {previous['name']} has {previous['follower_count']}M followers while {selection1['name']} has {selection1['follower_count']}M followers")
        print(f"Your current score: {score}")
    print(f"Compare A: {selection1['name']}, a {selection1['description']}, from {selection1['country']}.")

    print(vs)

    selection2 = choice(data)
    print(f"B: {selection2['name']}, a {selection2['description']}, from {selection2['country']}.")


    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if selection1['follower_count'] > selection2['follower_count']: correct = "a"
    elif selection1['follower_count'] < selection2['follower_count']: correct = "b"
    elif selection1['follower_count'] == selection2['follower_count']: correct = "draw"

    if user_guess == correct or correct == "draw":
        score += 1
        previous = selection1
        selection1 = selection2
    else: 
        print(f"You lose...\n{selection1['name']} has {selection1['follower_count']}M followers while {selection2['name']} has {selection2['follower_count']}M followers\nYour final score is {score}.")
        break
    if first is True: first = False
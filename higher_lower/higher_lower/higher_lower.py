import random
from game_data import data
from art import logo, vs

import os
def clear_console():
    os.system('cls')



def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

#Display art
print(logo)

score = 0
game_should_countinue = True

account_b = random.choice(data)

while game_should_countinue:
    #Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    #Format the account data into printable format 
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    #Ask for user guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    #Get follower count of each account
    follower_a = account_a['follower_count']
    follower_b = account_b['follower_count']


    is_correct = check_answer(guess, follower_a, follower_b)
    
    #Give feedback to user
    if is_correct:
        score += 1
        clear_console()
        print(logo)
        print(f"You're right! Current score: {score}")
    else:
        game_should_countinue = False
        print(f"Sorry, that's wrong. Final score: {score}")
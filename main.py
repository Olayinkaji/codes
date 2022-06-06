import random

game = ["R", "P", "S"]

while True:
    print("Welcome to Rock, Paper, Scissors game")
    user_name = input("Please type in your name:\n")
    print("Welcome", user_name.upper())
    user_action = input("Enter a choice caps lock: R for Rock P for Paper and S for Scissors\n".upper())

    # CPU side
    CPU = random.choice(game)
    print(f"You chose {user_action} and CPU chose {CPU}")
    if user_action == CPU:
        print(f"You both selected {user_action} It's a tie!")
    elif user_action == "R":
        if CPU == "S":
            print(f"Rock smashes scissors! {user_name} wins!")
        else:
            print(f"Paper covers rock! {user_name} lose.")
    elif user_action == "P":
        if CPU == "R":
            print(f"Paper covers rock! {user_name} wins!")
        else:
            print(f"Scissors cuts paper! {user_name} lose.")
    elif user_action == "S":
        if CPU == "P":
            print(f"Scissors cuts paper! {user_name} win!")
        else:
            print(f"Rock smashes scissors! {user_name} lose.")
    else:
        print("Sure you want to play, input is not valid! Try again")
    end = input("Would you like to play again? Y/N\n")
    if end == "N":
        print(f"Thank you for playing .........Sponsored by Zuri")
        break

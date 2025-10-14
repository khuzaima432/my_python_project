import random

item_list = ["Rock", "Paper", "Scissor"] 

user_choice = input("Enter your move, Rock, Paper, Scissor = ") 
computer_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {computer_choice}")

if user_choice == computer_choice:
    print("You Both Chooses The Same: Match Tie")

elif user_choice == "Rock":
    if computer_choice =="Paper":
        print("Paper Covers The Rock, Computer Win: ")
    else:
        print("Rock Break The Scissor, You Win!: ")

elif user_choice == "Paper":
    if computer_choice =="Scissor": 
        print("Scissor Cuts The Paper, Computer Win: ")
    else:
        print("Paper Covers The Rock, You Win!: ")
     
elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock Breaks The Scissor, Computer Win: ")
    else:
        print("Scissor Cuts The Paper, You Win!: ")
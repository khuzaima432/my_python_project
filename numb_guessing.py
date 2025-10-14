import random

comp_req = [1, 2, 3, 4, 5]

user_choice = int(input("Enter your guessed number (1 to 5): "))
computer_choice = random.choice(comp_req)

print(f"Your Choice = {user_choice}, Computer Choice = {computer_choice}")

if user_choice not in comp_req:
    print("Invalid Request! Please choose a number from 1 to 5.")
elif user_choice == computer_choice:
    print("🎉 You Win! You guessed it right!")
else:
    print("💻 You Lost! Computer Wins. Take the L.")

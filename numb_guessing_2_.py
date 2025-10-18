import random

computer_guess = random.randint(1, 100)

while True:
    try:
        user_choice = int(input("Enter your guess numb: "))
        if user_choice > computer_guess: 
            print("Too High")
        elif user_choice < computer_guess:
            print("Too low")
        else:
            print(" you guess it right you win horaay !!!!!!!!")
            break
    except ValueError:
        print("Please enter a vaild numb")
    
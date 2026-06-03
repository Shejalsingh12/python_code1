import random

# # Function for the game
# def guessing_game():
#     number_to_guess = random.randint(1, 40)  # computer picks a number
#     attempts = 0
    
#     # print("🎮 Welcome to the Number Guessing Game!")
#     # print("I have chosen a number between 1 and 20. Can you guess it?")

#     # Loop until user guesses correctly
#     while True:
#         guess = int(input("Enter your guess: "))
#         attempts += 1

#         # Conditional checks
#         if guess < number_to_guess:
#             print("Too low! Try again.")
#         elif guess > number_to_guess:
#             print("Too high! Try again.")
#         else:
#             print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
#             break  # exit loop when guessed correctly

# # Call the function
# guessing_game()

n=random.randint(1, 40)
attempts = 0

    # Loop until user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

        # Conditional checks
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
       print("🎉 Congratulations! You guessed the number in", attempts, "attempts.")
       break  
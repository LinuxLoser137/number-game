import random

def number_guessing_game():
	number = random.randint(1, 100)
	attempts = 0
	print("Welcome to the Number Guessing Game!")
	print("Guess a number between 1 and 100")

	while True:
		try:
			guess =int(input("Enter your guess: "))
			attempts += 1

			if guess < number:
				print("Higher! Guess Again!")
			elif guess > number:
				print("Lower! Guess Again!")
			else:
				print(f"You Win! You guesed the number {number}")
				break

		except ValueError:
				print("Error. Enter a valid number")
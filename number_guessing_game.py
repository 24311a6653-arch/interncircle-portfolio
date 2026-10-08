import random

print("===== NUMBER GUESSING GAME =====")

number = random.randint(1, 100)
attempts = 0

print("I have chosen a number between 1 and 100.")
print("Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the number!")
        print("Attempts:", attempts)

        score = 100 - (attempts - 1) * 10

        if score < 10:
            score = 10

        print("Your score:", score)
        break

print("Thank you for playing!")
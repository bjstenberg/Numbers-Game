from art import logo
import random
import clear

print(logo)

answer = random.randint(0, 100 + 1)

lives = 0

print("Welcome to the Number Guessing game!")
print("I am currently thinking about a number between 1 and 100. Can you guess which one I am thinking of?")
print(f"Psst The number is {answer}")
difficulty = input("Please select your difficulty level. 'Easy' or 'Hard': ").lower()


def start_lives():
    global lives
    if difficulty == 'easy':
        lives += 10
        print(f"You have {lives} lives.")
    elif difficulty == 'hard':
        lives += 5
        print(f"You have {lives} lives.")


start_lives()

game = True

while game:

    guess = int(input("Make a guess: "))

    def lives_left():
        global lives
        global game
        if guess == answer:
            print("That is correct! Well done!")
            game = False
        elif guess < answer:
            print("Too low, guess again: ")
            lives -= 1
            print(f"You have {lives} lives remaining.")
        elif guess > answer:
            print("Too high! Guess again: ")
            lives -= 1
            print(f"You have {lives} lives remaining.")

    lives_left()

    if lives == 0:
        print(f"You lost, you have {lives} lives left.")
        game = False









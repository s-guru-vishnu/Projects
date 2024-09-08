import random

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()

else:
    print("Please type a number next time")
    quit()

r = random.randint(1, top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess : ")
    if guess.isdigit():
        guess = int(guess)

    else:
        print("Please type a number next time")
        continue

    if guess == r:
        print("Your guess is correct")
        print("You got the guess in", guesses, "chance(s)")
        break
    else:
        print("Sorry, Your guessing is wrong please try again")

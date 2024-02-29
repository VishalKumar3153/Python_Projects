import random

top_of_range=input("Type a upper range number for your guess: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Enter a number greater than 0 next time. ")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0
while True:
    number_guess=input("Make a Guess: ")
    guesses+=1
    if number_guess.isdigit():
        number_guess=int(number_guess)

    else:
        print("Please type a number next time.")
        continue

    if number_guess == random_number:
        print("You got it :)")
        break
    elif number_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number")
print("You got it in",guesses, "guesses")


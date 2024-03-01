import emoji
import random

options=["rock","paper","scissor"]
user_wins=0
computer_wins=0
while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_num=random.randint(0,2)
    computer_input=options[random_num]
    print("Computer picks",computer_input)
    if user_input=="rock" and computer_input=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input=="paper" and computer_input=="rock":
        print("You won!")
        user_wins+=1
    elif user_input=="scissors" and computer_input == "paper":
        print("You won!")
        user_wins+=1
    elif user_input == computer_input:
        print("Yeah,Both are Same,Try again!"+emoji.emojize(":grinning_face_with_big_eyes:"))
        continue
    else:
        print("You lost!")
        computer_wins+=1

print("You won",str(user_wins) + " times.")
print("Computer won",str(computer_wins) + " times.")
print("Good Bye!,Have a nice day :)")
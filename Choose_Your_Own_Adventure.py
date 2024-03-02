name= input("Type your name: ")

print("Welcome",name,"to this adventure!")

answer = input("you are on the dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right) ").lower()

if answer=="left":
    answer2= input("You come to river, you can walk around it or swim across? Type walk to walk around or swim to swim across the river (walk/swim) ").lower()
    if answer2 == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer2== "walk":
        print("You walked for many miles, ran out of water and you lost the game!")
    else:
        print("Not a valid option. You lose!")
elif answer=="right":
     answer2= input("You come to the bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
     if answer2 == "back":
        print("You go back and lose.")
     elif answer2== "cross":
        answer2=input("You cross the stranger and meet a stranger. Do you talk to them(yes/no)? ").lower()
        if answer2== "yes":
             print("You talk to the stranger and they give you diamond. You WIN :)")
        elif answer2== "no":
             print("You ignored the stranger and they affended you.You lost!!!")
        else:
         print("Not a valid option. You lose!")
     else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")
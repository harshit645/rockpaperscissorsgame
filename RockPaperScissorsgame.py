import random


flag=0
while flag==0:

    user_choice=input("enter the user choice")
    user_choice=user_choice.upper()
    print("user_choice",user_choice)


    values=['ROCK','PAPER','SCISSORS']
    x=random.randint(0,2)
    computer_choice=values[x]
    print("computer_choice",computer_choice)


    if user_choice==computer_choice:
        print("BOTH CHOOSE SAME THING")

    else:
        if user_choice=='ROCK':
            if computer_choice=='PAPER':
                print("computer_choice wins over user_choice")

            elif computer_choice=='SCISSORS':
                print("user_choice wins over computer_choice")


        elif user_choice=='PAPER':
            if computer_choice=='ROCK':
                print("user_choice wins over computer_choice")

            elif computer_choice=='SCISSORS':
                print("computer_choice wins over user_choice")


        elif user_choice == 'SCISSORS':
            if computer_choice == 'ROCK':
                print("computer_choice wins over user_choice")

            elif computer_choice == 'PAPER':
                print("user_choice wins over computer_choice")


        else:
            print("Wrong Input was given by user")


    choice=input("do you want to play again Y/N")
    choice=choice.upper()

    if choice=='N':
        flag=1

    elif choice=='Y':
        flag=0


    else:
        print("I don't understand")
        break

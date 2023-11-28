from random import randint


def silgame():
    gamech= randint(0,100)
    mynum= input("Enter your number between 0 and 100 here: ")
    int(mynum)

    if gamech==mynum:
        print("Yay, you guessed right")
    else:
        print("That's a shame, you lost")
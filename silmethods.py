from random import randint


def silgame(getal):
    gamech= randint(0,100)
    #mynum= input("Enter your number between 0 and 100 here: ")
    mynum= int(getal)
    int(mynum)

    if gamech==mynum:
        print("Yay, you guessed right")
    else:
        print("That's a shame, you lost")
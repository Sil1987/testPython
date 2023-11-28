from random import randint


def silgame(getal):
    gamech= randint(0,3)
    #mynum= input("Enter your number between 0 and 100 here: ")
    mynum= int(getal)
    int(mynum)

    if gamech==mynum:
        return "Yay, you guessed right"
    else:
        return "That's a shame, you lost"
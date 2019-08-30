# HenryCalderonMadLibs
# IDE/OS: Atom/ MAC OS
# August 28, 2019
# Purpose: Creating a MadLinbs game in Python

inputWords = list()
story1Words = ["Noun","Adj","Verb"]

def takeInput(list):
    #Taking in the words from user and assigning it to an array for use later
    return 0

#Stuff
def chooseStory():
    if choice == 1:
        return 0
    else:
        print("Try Again")

def createStory():
    return 0



def MadGame():
    on = True
    while on:
        print("Madlibs! The Creative Story Game")
        print("--------------------------------")
        print("Choose A Story: ")
        print(" 1) A Man of Taste")
        print("Q = Quit")
        choice = input("Which Story?: ")
        if choice == 1:
            createStory()
        elif choice == Q:
            on = False
        else:
            print("Sorry, That isn't an option.")

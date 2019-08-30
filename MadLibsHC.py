# HenryCalderonMadLibs
# IDE/OS: Atom/ MAC OS
# August 28, 2019
# Purpose: Creating a MadLinbs game in Python

inputWords = list()
story1Words = ["Noun","Adj","Verb"]

# def takeInput(list):
#     #Taking in the words from user and assigning it to an array for use later
#     return 0

def createStory(list):
    for i in range(0,len(list)):
        wordChoice = input("Enter a " + list[i] + ": ")
        #print("Give a "+)
        list[i] = wordChoice
    print(list)



def MadGame():
    on = True
    while on:
        print("Madlibs! The Creative Story Game")
        print("--------------------------------")
        print("Choose A Story: ")
        print(" 1) Egg")
        print("Q = Quit")
        choice = input("Which Story?: ")

        if choice == "1":
            createStory(story1Words)
        elif choice == "Q":
            on = False
        else:
            print("Sorry, That isn't an option")

MadGame()

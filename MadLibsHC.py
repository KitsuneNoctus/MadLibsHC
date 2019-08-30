# HenryCalderonMadLibs
# IDE/OS: Atom/ MAC OS
# August 28, 2019
# Purpose: Creating a MadLinbs game in Python

inputWords = ["None"]
story1Words = ("Noun","Adj","Verb")

# def takeInput(list):
#     #Taking in the words from user and assigning it to an array for use later
#     return 0

def createStory(listOfWords):
    storedList = list(listOfWords)
    for i in range(0, len(listOfWords)-1):
        storedList[i] = input("Enter a " + listOfWords[i] + ": ")
        # inputWords[i].append(wordChoice)
    #print(storedList)


# def printStory(choice, wordsGiven):
#     story1 = ["Hi There ","You look ","Keep on the "]
#     if choice == 1:
#         storyChoice = story1
#     else:
#         print("Nothing Selected")
#
#     for i in range(0, len(storyChoice)):
#         print(storyChoice[i]+ wordsGiven[i])



def MadGame():
    on = True
    while on:
        print("Madlibs! The Creative Story Game")
        print("--------------------------------")
        print("Choose A Story: ")
        print(" 1) Egg")
        print("Q = Quit")
        inputWords.clear()
        choice = input("Which Story?: ")

        if choice == "1":
            createStory(story1Words)
            # printStory(choice, inputWords)
        elif choice == "Q":
            on = False
        else:
            print("Sorry, That isn't an option")

MadGame()
print(story1Words)

# HenryCalderonMadLibs
# IDE/OS: Atom/ MAC OS
# August 28, 2019
# Purpose: Creating a MadLinbs game in Python
import string
import random
#inputWords = ["None"]
#Tuple list to make sure contents dont change
story1Words = ("Noun","Number","Noun","Verb","Adj","Verb ending in 'ing'","Adj","Adj","Noun","Name")
story2Words = ("Adj","Noun","Adj ending with -est","Noun")

adjList = ("Sour","Moist","Smelly","Clean","Annoying","Tired")
nounList = ("Burrito","Chihuahua","Egg","Mouse","Pokeball")
verbList = ("Run","Cry","Scream","Fly","Drop","Fight")
numList = ("200","10","3","9","80")
verbingList = ("Running","Falling","Eating","Crying","Smiling")
adjestList = ("Sweetest","Coldest","Hardest","Pinkest")
nameList = ("Ben","Lewis","Trystan","Lex")

# def takeInput(list):
#     #Taking in the words from user and assigning it to an array for use later
#     return 0

def createStory(listOfWords):
    storedList = list(listOfWords)
    userEnter = input("Would you like to let the computer decide the story? [Y]/[Any other button and you choose]: ")
    if userEnter == "Y" or userEnter == "Yes" or userEnter == "y":
        for i in range(0, len(listOfWords)):
            print("Meow")
    else:
        for i in range(0, len(listOfWords)):
            improperInput = True
            checked = True
            #storedList[i] = input("Enter a " + listOfWords[i] + ": ")
            while improperInput:
                takenInput = input("Enter a " + listOfWords[i] + ": ")
                checked = isInputOkay(takenInput)
                if checked == False:
                    print("Improper Input, Try Again.")
                else:
                    storedList[i] = takenInput
                    improperInput = False


    #print(storedList)
    return storedList


def isInputOkay(inputForList):

    if inputForList == "":
        return False
    elif inputForList in string.punctuation:
        #https://www.geeksforgeeks.org/string-punctuation-in-python/
        return False
    else:
        return True


def printStory(choice, wordsGiven):
    # story1 = ("There once was a man who lived on a ",". He owned "," egg cups, which he holdsmost dear. One day a giant ",
    # " struck his home, making all the egg cups ",". His ", " egg cups were now a mess. The man was ", " around tyring to clean up. It took him hours, but he was very ",
    # " once he was done. He noticed that that his favorite ", " egg cupwas missing. He ran all up and down the ", " looking for it. Alas, it was nowhere to be found, and so ",
    # " went home with one less egg cup")
    print("------------Story-------------")
    if choice == 1:
        print("There once was a man who lived on a "+wordsGiven[0]+". He owned "+wordsGiven[1]+" egg cups, which he holds most dear. One day a giant "+wordsGiven[2]+
        " struck his home, making all the egg cups "+wordsGiven[3]+". His "+wordsGiven[4]+" egg cups were now a mess. The man was "+wordsGiven[5]+" around trying to clean up. It took him hours, but he was very "+wordsGiven[6]+
        " once he was done. He noticed that that his favorite "+wordsGiven[7]+" egg cup was missing. He ran all up and down the "+wordsGiven[8]+" looking for it. Alas, it was nowhere to be found, and so "+wordsGiven[9]+
        " went home with one less egg cup.")
        #storyChoice = list(story1)
    if choice == 2:
        print("Hello you absolute "+wordsGiven[0]+" "+wordsGiven[1]+". You better try your "+wordsGiven[2]+" today you "+wordsGiven[3]+".")
    else:
        print("Nothing Selected")

    print("------------------------------")
    # print(len(story1))
    # print(len(wordsGiven))

    wholeStory = ""
    # for i in range(0, len(storyChoice)):
    #     wholeStory += storyChoice[i]+ wordsGiven[i]
    # print("------------Story-------------")
    # print(wholeStory + ".")
    # print("------------------------------")



#Based this menu off a game I made in a previous college course.
def MadGame():
    on = True
    while on:
        print("-*----------------------------*-")
        print("Madlibs! The Creative Story Game")
        print("-*----------------------------*-")
        print("Choose A Story: ")
        print(" 1) The Man and His Cups")
        print(" 2) Short and Sweet.")
        print("Q = Quit")

        choice = input("Which Story?: ")

        if choice == "1":
            choice = 1
            #createStory(story1Words)
            printStory(choice, createStory(story1Words))
        if choice == "2":
            choice = 2
            #createStory(story1Words)
            printStory(choice, createStory(story2Words))
        elif choice == "Q" or choice == "q" or choice == "Quit":
            on = False
        else:
            print("Sorry, That isn't an option")

MadGame()
#print(story1Words)

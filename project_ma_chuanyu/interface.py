# ITP 115, Fall 2024
# Final Project
# Name: Chuanyu Ma
# Email: chuanyum@usc.edu
# Section: piethon
# Filename: interface.py (update accordingly)
# Description: final project

import helper
import pretty_print
#import the functions from other files

def displayRules(textfileStr="rules.txt"):
    fileRead = open(textfileStr, "r") #read the file and print the rules
    for line in fileRead:
        line = line.strip() #clean the blank line
        print(line)
    fileRead.close()

def isValidNumber(userStr, startNum, endNum):
    if userStr.isdigit(): #check whether user's input is numer
        userNum=int(userStr)
        startNum=int(startNum)
        endNum=int(endNum) #cancatinate them into integer
        if startNum<=userNum<=endNum:
            return True
    return False

def pickPuzzle(puzzleList):
    length=len(puzzleList)
    length=str(length)
    userinput=input("Enter a puzzle number (1-"+length+"): ")
    while not isValidNumber(userinput, 1, length):
        userinput = input("Enter a puzzle number (1-" + length + "): ") #get user input
    selectedPuzzle=helper.getPuzzle(puzzleList, userinput)
    return selectedPuzzle

def getGuessList(wordList):
    print("Enter four items for your guess")
    guess=[]
    for i in range(4):#get 4 user input
        userInput=input("Item #"+str(i+1)+": ")
        while userInput not in wordList or userInput in guess: #avoid user input invalid or repeat
            userInput = input("Item #" + str(i+1) + ": ")
        guess.append(userInput)
    guess.sort() #sort them in alphabetic order
    return guess

def checkConnection(puzzleDict, guessList):
    returnValue=0 #return 0 if no connection
    for i in range(1, 5):
        group = helper.getWordsInGroup(puzzleDict, i)
        if guessList== group:
            returnValue = i
    return returnValue

def savePuzzle(puzzleDict, groupsFound=[1,2,3,4]):
    puzzleNum=puzzleDict["num"]
    saveFileName=puzzleNum+".txt"
    fileWrite=open(saveFileName, "w") #write a file
    puzzleDate = puzzleDict["date"]
    print(puzzleDate, file=fileWrite) #write the date in file
    fileWrite.close()
    print("Puzzle from "+puzzleDate+" has been saved to "+saveFileName)

def playGame(puzzleDict):
    groupsFound=[]
    mistake=0
    while len(groupsFound)<4 and mistake <4: #display the game
        pretty_print.displayGrid(puzzleDict, groupsFound,mistake) #call the pretty print function
        unconnectedWords = helper.getUnconnectedWords(puzzleDict, groupsFound)
        guessList = getGuessList(unconnectedWords)
        difficulty = checkConnection(puzzleDict, guessList)
        if difficulty != 0:
            if difficulty not in groupsFound:
                groupsFound.append(difficulty)
        else:
            mistake+=1
    if mistake>=4: #fail the game
        pretty_print.displayGrid(puzzleDict)
        print("Better luck next time.")
        savePuzzle(puzzleDict) #except the puzzleDict, other parameter use default value
    else:
        pretty_print.displayGrid(puzzleDict, groupsFound)
        print("Congratulations!")
        savePuzzle(puzzleDict, groupsFound)
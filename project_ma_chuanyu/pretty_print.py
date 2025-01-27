# ITP 115, Fall 2024
# Final Project
# Name: Trina Gregory
# Filename: pretty_print.py
# Description: This file contains functions to print a puzzle using colors

import helper
import random
import pickle

# Function: loadData
# Parameter: filenameStr with a default value of connections_data.bin
# Return value: a list of dictionaries where each dictionary represents one puzzle.
# This function reads the binary file and creates a list of puzzles.
def loadData(filenameStr="puzzles.bin"):
    # use pickle
    fileObj = open(filenameStr, "rb")
    puzzleList = pickle.load(fileObj)
    fileObj.close()
    return puzzleList

# Function: loadData
# Parameter 1: puzzleList is the list to dump to a binary file
# Parameter 2: filenameStr with a default value of connections_data.bin
# Return value: None
# This function write the puzzleList to the binary file.
def dumpData(puzzleList, filenameStr="puzzles.bin"):
    # pickle
    fileObj = open(filenameStr, "wb")
    pickle.dump(puzzleList, fileObj)
    fileObj.close()

# Function: getColorCode
# Parameter: colorStr is a str with a name of a color
# Return value: a str with the ANSI code
# Color codes for ANSI, https://www.hackitu.de/termcolor256/
def getColorCode(colorStr):
    colorDict = {"YELLOW": "\x1b[48;5;220m", "GREEN": "\x1b[48;5;070m", "BLUE": "\x1b[48;5;111m",
                 "PURPLE": "\x1b[48;5;135m", "GREY": "\x1b[48;5;255m", "RESET": "\u001B[0m",
                 "BLACK": "\x1b[30m"}
    if colorStr.upper() in colorDict:
        return colorDict[colorStr]
    else:
        print("pretty_print.getColorCode: invalid colorStr")
        return colorDict["GREY"]

# Function: randomizeList
# Parameter: wordList is a list of strings
# Return value: a list of strings which are the same strings from wordList but in a random order
# This function randomly gets items from the wordList to create a new list and returns the new list.
def randomizeList(wordList):
    randomList = []
    while wordList:
        randomItem = random.choice(wordList)
        randomList.append(randomItem)
        wordList.remove(randomItem)
    return randomList

# Function: longestWordLength
# Parameter: wordList is a list of strings
# Return value: an int with the length of the longest word in the wordList
def longestWordLength(wordList):
    max = 0
    for word in wordList:
        if len(word) > max:
            max = len(word)
    return max

# Function: getSpaces
# Parameter 1: infoStr is a str
# Parameter 2: wordMax is an int with a default value of 6
# Parameter 3: numSpaces is an int with a default value of 3
# Return value: a str with spaces
def getSpaces(infoStr, wordMax=6, numSpaces=3):
    rowLen = (wordMax + numSpaces) * 4
    strLen = len(infoStr)
    diff = rowLen - strLen
    half = diff // 2
    return " " * half

# Function: displayGroup
# Parameter 1: wordList is a list of words to display
# Parameter 2: colorStr is a str with the name of the color to display
# Parameter 3: connectStr is a str with the connection str
# Parameter 4: wordMax is an int with a default value of 6
# Return value: None
def displayGroup(wordList, colorStr, connectStr, wordMax=6):
    ansiCode = getColorCode(colorStr)
    fgCode = getColorCode("BLACK")
    spacesBefore = getSpaces(connectStr, wordMax)
    spacesAfter = spacesBefore
    if len(connectStr) % 2 == 1:
        spacesAfter += " "
    print(fgCode + ansiCode + spacesBefore + connectStr + spacesAfter, end="")
    print(getColorCode("RESET"))
    groupStr = ", ".join(wordList)
    spacesBefore = getSpaces(groupStr, wordMax)
    spacesAfter = spacesBefore
    if len(groupStr) % 2 == 1:
        spacesAfter += " "
    print(fgCode + ansiCode + spacesBefore + groupStr + spacesAfter, end="")
    print(getColorCode("RESET"))

# Function: displayRow
# Parameter 1: wordList is a list of words to display
# Parameter 2: colorStr is a str with the name of the color to display with a default value of "GREY"
# Parameter 3: wordMax is an int with a default value of 6
# Parameter 4: numSpaces is an int with a default value of 3
def displayRow(wordList, colorStr="GREY", wordMax=6, numSpaces=3):
    ansiCode = getColorCode(colorStr)
    fgCode = getColorCode("BLACK")
    endStr = " " * numSpaces
    for word in wordList:
        wordSize = len(word)
        if wordSize < wordMax:
            diff = wordMax - wordSize
            word = word + " " * diff
        print(fgCode + ansiCode + word, end=endStr)
    print(getColorCode("RESET"))

# Function: displayGrid
# Parameter 1: puzzleDict is a dictionary representing one puzzle
# Parameter 2: foundGroupList is a list of integers with the difficulty numbers of the groups that have been found
# and has a default value of [1, 2, 3, 4]
# Parameter 3: mistakes is an integer with the number of mistakes used to display the mistakes remaining message
# and has a default value of -1 (which means do not display the mistakes message)
# Return value: None
def displayGrid(puzzleDict, foundGroupList=[1, 2, 3, 4], mistakes=-1):
    if type(puzzleDict) != dict:
        print("pretty_print.displayGrid: puzzleDict parameter needs to be a dictionary.")
        print("\tUnable to display the grid.")
        return
    if len(puzzleDict) == 0:
        print("pretty_print.displayGrid: puzzleDict parameter needs to be a non-empty dictionary.")
        print("\tUnable to display the grid.")
        return
    if type(foundGroupList) != list:
        print("pretty_print.displayGrid: foundGroupList parameter needs to be a list.")
        print("\tUnable to display the grid.")
        return
    if type(mistakes) != int:
        print("pretty_print.displayGrid: mistakes parameter needs to be an integer.")
        print("\tUnable to display the grid.")
        return

    spacesAfterWord = 3
    numWordsInRow = 4
    wordList = helper.getUnconnectedWords(puzzleDict, foundGroupList)
    if type(wordList) != list:
        print("pretty_print.displayGrid: helper.getUnconnectedWords() does not return a list.")
        print("\tUnable to display the grid.")
        return
    size = len(wordList)
    if size > 0:
        if type(wordList[0]) != str:
            print("pretty_print.displayGrid: helper.getUnconnectedWords() does not return a list of strings.")
            print("\tAre you returning a list of lists of strings?")
            print("\tUnable to display the grid.")
            return

    allWordList = helper.getUnconnectedWords(puzzleDict, [])
    if type(allWordList) != list:
        print("pretty_print.displayGrid: helper.getUnconnectedWords() does not return a list.")
        print("\tUnable to display the grid.")
        return
    allSize = len(allWordList)
    if allSize > 0:
        if type(allWordList[0]) != str:
            print("pretty_print.displayGrid: helper.getUnconnectedWords() does not return a list of strings.")
            print("\tAre you returning a list of lists of strings?")
            print("\tUnable to display the grid.")
            return
    else:
        print("pretty_print.displayGrid: helper.getUnconnectedWords() returned an empty list.")
        print("\tUnable to display the grid.")
        return

    wordLen = longestWordLength(allWordList)
    connection = helper.getConnection(puzzleDict, 1)
    if not connection or type(connection) != str:
        print("pretty_print.displayGrid: helper.getConnection() did not return a non-empty string.")
        print("\tUnable to display the grid.")
        return
    longestConnection = len(connection)
    for difficultyNum in range(2, 5):
        connection = helper.getConnection(puzzleDict, difficultyNum)
        if not connection or type(connection) != str:
            print("pretty_print.displayGrid: helper.getConnection() did not return a non-empty string.")
            print("\tUnable to display the grid.")
            return
        connectionLen = len(connection)
        if connectionLen > longestConnection:
            longestConnection = connectionLen
    if (wordLen + spacesAfterWord) * numWordsInRow < longestConnection:
        wordLen = (longestConnection + spacesAfterWord) // numWordsInRow - spacesAfterWord

    print()
    message = "Create four groups of four!"
    spaces = getSpaces(message, wordLen)
    print(spaces + message)
    for num in foundGroupList:
        rowList = helper.getWordsInGroup(puzzleDict, num)
        if type(rowList) != list:
            print("pretty_print.displayGrid: helper.getWordsInGroup() did not return a list.")
            print("\tUnable to display the grid.")
            return
        connectStr = helper.getConnection(puzzleDict, num)
        if not connectStr or type(connectStr) != str:
            print("pretty_print.displayGrid: helper.getConnection() did not return a non-empty string.")
            print("\tUnable to display the grid.")
            return
        colorStr = helper.getColor(puzzleDict, num)
        if not colorStr or type(colorStr) != str:
            print("pretty_print.displayGrid: helper.getColor() did not return a non-empty string.")
            print("\tUnable to display the grid.")
            return

        displayGroup(rowList, colorStr, connectStr, wordLen)

    wordList = randomizeList(wordList)
    rows = size // numWordsInRow
    for row in range(rows):
        startIndex = row * numWordsInRow
        stopIndex = startIndex + numWordsInRow
        rowList = wordList[startIndex:stopIndex]
        displayRow(rowList, "GREY", wordLen)
    if mistakes >= 0:
        remain = 4 - mistakes
        message = "Mistakes remaining: " + "* " * remain
        spaces = getSpaces(message, wordLen)
        print(getColorCode("RESET") + spaces + message)

    print(getColorCode("RESET"))

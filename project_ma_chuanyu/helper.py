# ITP 115, Fall 2024
# Final Project
# Name: Chuanyu Ma
# Email: chuanyum@usc.edu
# Section: piethon
# Filename: helper.py (update accordingly)
# Description: final project

#read the file
def createPuzzleList(fileNameStr="puzzles.csv"):
    fileRead=open(fileNameStr, "r")
    firstLine=fileRead.readline()
    firstLine=firstLine.strip()
    firstLineList=firstLine.split(",") #get list from the file

#create empty list for file
    puzzleList=[]
    for line in fileRead:
        lineCleaned=line.strip()
        lineList=lineCleaned.split(",")
        puzzleDict={}
        for i in range(len(firstLineList)):
            puzzleDict[firstLineList[i]]=lineList[i]
        puzzleList.append(puzzleDict) #put the line in list
    fileRead.close()
    return puzzleList

def getPuzzle(puzzleList, numStr):
    for i in puzzleList:
        if "num" in i:
            if i["num"]==numStr:
                return i
    return {} #return empty dictionary if did not get puzzle

def getColor(puzzleDict, difficultyNum):
    key = "color" + str(difficultyNum) #name the key
    if key in puzzleDict:
        return puzzleDict[key]
    else:
        return "GREY"

#name the key
def getConnection(puzzleDict, difficultyNum):
    key = "connection" + str(difficultyNum) #name the key
    if key in puzzleDict:
        return puzzleDict[key]
    else:
        return "CONNECTION ERROR"

def getWordsInGroup(puzzleDict, difficultyNum):
    words=[]
    for i in range(1, 5):
        key="word"+str(difficultyNum)+str(i)
        if key in puzzleDict:
            words.append(puzzleDict[key])
    words.sort() #alphabetically order
    return words


def getUnconnectedWords(puzzleDict, foundGroupList):
    unconnectedWords=[]
    for i in range(1, 5):
        if i not in foundGroupList:
            words=getWordsInGroup(puzzleDict, i) #call last function to get sorted words
            for k in words:
                unconnectedWords.append(k)
    return unconnectedWords


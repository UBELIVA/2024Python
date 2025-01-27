# ITP 115, Fall 2024
# Final Project
# Name: Chuanyu Ma
# Email: chuanyum@usc.edu
# Section: pie-thon
# Filename: main_chuanyu_ma
# Description: final project

import helper
import interface
import pretty_print

def main():
    print("Connections!")
    print("Group words that share a common thread.")
    interface.displayRules() #rules
    puzzleList=helper.createPuzzleList() #get puzzle list
    pretty_print.loadData() #display puzzle
    selectedPuzzle = interface.pickPuzzle(puzzleList)
    interface.playGame(selectedPuzzle)

main()

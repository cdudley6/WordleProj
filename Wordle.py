# File: Wordle.py

"""
author: Busbyberkly Peterson 9/11/23
 file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter as tk
from tkinter import simpledialog

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR


# This function asks the user what color-scheme they would like and implements their choice
def get_color_scheme():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    color_scheme = simpledialog.askstring("color-scheme", "Welcome to Wordle! Please pick your color-scheme.\n Enter 'default' or 'color-blind':")

    # Check if the user entered a valid option
    if color_scheme and color_scheme.lower() in ('default', 'color-blind'):
        return color_scheme.lower()
    else:
        print("Invalid input. Using default color scheme.")
        return 'default'

def wordle():

    sColor_scheme = get_color_scheme()
    if sColor_scheme == "default":
        # Default color-scheme
        CORRECT_COLOR = "#66BB66"       # Light green for correct letters
        PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters     
    else: 
        # The Color-blind scheme colors
        CORRECT_COLOR = "#006CD1"  #Light blue for correct letters
        PRESENT_COLOR = "#994F00" # Golden Brown for misplaced letters

    def enter_action(s):
        #converting the user input into a string and making it lowercase so that compared to the word dictionary 
        line = str(s).lower()

        #get a random word from the word dictionary
        # randomword = random.chbeoice(FIVE_LETTER_WORDS)
        if line in FIVE_LETTER_WORDS:
            #gw.show_message("Good Job.")
            gw.show_message(hidden)
            #this is where we implement the colors and comparison to the hidden random word
            for (iCount) in range(N_COLS):
                solution = hidden[iCount]
                user = line[iCount]
                #if the user-generated letter is the same as the letter in the solution turn the key GREEN
                if user == solution:
                    gw.set_square_color(0,iCount, CORRECT_COLOR)
                elif user in hidden:
                    gw.set_square_color(0, iCount, PRESENT_COLOR)



        else:
            gw.show_message("Not in word list.")
            
        
    

    gw = WordleGWindow()
    
    randomword = random.choice(FIVE_LETTER_WORDS)
    hidden = str(randomword)

    # loop to get each letter from the random word to the letter boxes.
    # for (iCount) in range(N_COLS):
    #     letter = randomword[iCount]
    #     gw.set_square_letter(0, iCount, letter)
   
    
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()

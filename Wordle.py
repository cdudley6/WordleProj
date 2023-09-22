# File: Wordle.py

"""
author: Busbyberkly Peterson 9/11/23
 file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR

def wordle():

    def enter_action(s):
        
        #converting the user input into a string and making it lowercase so that compared to the word dictionary 
        line = str(s).lower()

    
        row = gw.get_current_row()
        
        if line in FIVE_LETTER_WORDS:
            #gw.show_message("Good Job.")
            gw.show_message(hidden)
            
            #this is where we implement the colors and comparison to the hidden random word
            for (iCount) in range(N_COLS):
    
                solution = hidden[iCount].upper()
                user = line[iCount].upper()
                
                #if the user-generated letter is the same as the letter in the solution turn the key GREEN
                if user == solution:
               
                    gw.set_square_color(row,iCount, CORRECT_COLOR)
        
        else:
            gw.show_message("Not in word list.")
        
        row = row + 1
        gw.set_current_row(row)
    
    gw = WordleGWindow()
    

    randomword = random.choice(FIVE_LETTER_WORDS)
    hidden = str(randomword)

    #milestone 1
    # loop to get each letter from the random word to the letter boxes.
    # for (iCount) in range(N_COLS):
    #     letter = randomword[iCount]
    #     gw.set_square_letter(0, iCount, letter)
    
       
    gw.add_enter_listener(enter_action)
 
# Startup code

if __name__ == "__main__":
    wordle()

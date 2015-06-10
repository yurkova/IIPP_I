"""
Guess the number" mini-project.
Input will come from buttons and an input field.
All output for the game will be printed in the console.
"""

import simplegui
import random
import math

secret_number = 8
range = 100
guesses_counter = 7

# helper function to start and restart the game
def new_game():
    global secret_number, guesses_counter
    secret_number = random.randrange(0, range)
    guesses_counter = int(math.ceil(math.log(range, 2)))
    print ""
    print "New game. Range is from 0 to ", range
    print "Number of remaining guesses is", guesses_counter

# define event handlers for control panel
def range100():
    global range
    range = 100
    new_game()

def range1000():
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guesses_counter
    guess_number = int(guess)
    print "Guess was", guess_number
    if(guess_number == secret_number):
        print "Correct!"
        new_game()
    else:
        if(guess_number < secret_number):
            print "Higher!"
        elif(guess_number > secret_number):
            print "Lower!"
        guesses_counter -= 1
        if(guesses_counter > 0):
            print "Number of remaining guesses is", guesses_counter
        else:
            print "You ran out of guesses.  The number was", secret_number
            new_game()

    
# create frame
frame = simplegui.create_frame("Guess the number!", 300, 200)
frame.add_input("Guess:", input_guess, 114)
frame.add_button("Range: 0-100", range100, 120)
frame.add_button("Range: 0-1000", range1000, 120)
frame.start()

# call new_game 
new_game()


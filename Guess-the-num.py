# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# made by j.z. on 10/20/15

import simplegui
import random
import math


num_range = 100
guessrand = 0
secret_number = 0
gcount = 0

# helper function to start and restart the game
##initialize global variables, guess times is computed 
##based on binary search

def new_game():
    global num_range, secret_number, gcount 
    secret_number = random.randrange(0, num_range)
    gcount = int(math.ceil( math.log(num_range + 1, 2)))
    
def out_put():
    global guessrand, secret_number, gcount
   
    ####print "Secret_number ", secret_number
    ####compare and show result
    gcount = gcount - 1
    if gcount >= 0:
        print "Guess was ", guessrand
        if guessrand < secret_number:
            print "Please go Higher"
            print "Guess times left: ",gcount, "\n"
        elif guessrand == secret_number:
            print "Correct! The secret number is ", secret_number
            print "You won! Please start a new game.\n"
            pass
            new_game()
            print "This is start of a new game" 
        else:
            print "Please go Lower"
            print "Guess times left: ",gcount, "\n"
    else:
        print "Oops, you lost and no more guesses. Good luck next time."
        print "Please start for a new game.\n"
        pass
        new_game()
        print "This is start of a new game"
                    
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guessrand
    guessrand = float(guess)
    out_put() 
   
   

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 150)
f.add_button("Range is [0, 1000)", range1000, 150)
f.add_input("Input your guess and hit Enter", input_guess, 200)

# call new_game 
new_game()
f.start() 



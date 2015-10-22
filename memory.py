# implementation of card game - Memory
# made by j.z on 10/17/15

import simplegui
import random


# helper function to initialize globals
def new_game():
    global deck_cards,exposed, turns,state
    state = 0
    turns = 0
    deck_cards = range(8)
    deck_cards.extend(deck_cards) 
    random.shuffle(deck_cards) 
    exposed = [False for i in deck_cards] 
 
     
# define event handlers, follwing mini instruction
def mouseclick(pos):
    # add game state logic here
    global deck_cards, state, turns, firstcard,secondcard
    clickcard = int(pos[0] / 50)
    if state == 0:
        firstcard = clickcard
        exposed[firstcard] = True
        state = 1
    elif state == 1:
        if not exposed[clickcard]:
            secondcard = clickcard
            exposed[secondcard] = True
            state = 2
            turns += 1
    elif state == 2:
        if not exposed[clickcard]:
            if deck_cards[firstcard] == deck_cards[secondcard]:
                pass
            else:
                exposed[firstcard] = False
                exposed[secondcard] = False
            firstcard = clickcard
            exposed[firstcard] = True
            state = 1
    label.set_text("Turns = " + str(turns)) 
    pass
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(deck_cards)):
        wid = i*50
        if exposed[i]:
            canvas.draw_text(str(deck_cards[i]),(wid+10,55),44,'red','sans-serif')
        else:
             canvas.draw_polygon([(wid,0),(wid+50,0),(wid+50,100),
                             (wid,100)], 4,'grey')
           
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



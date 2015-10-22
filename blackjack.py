# Mini-project #6 - Blackjack
##made by j.z. on 10/21/2015

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
action = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = [] 	# create Hand object
        
    def __str__(self):  # return a string representation of a hand
        self.list = "Hand contains:"
        for card in self.cards:
            self.list +=  " "  + card.__str__()
        return self.list
       
    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand
        
    def get_value(self):
        self.value = 0
        acecount = 0
# count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
# compute the value of the hand, see Blackjack video
#at most one ace need to count as 11
        for card in self.cards:
             self.value += VALUES[Card.get_rank(card)]   
             if Card.get_rank(card) == 'A':
                    acecount += 1
        if acecount > 0 and self.value <= 10:
                    self.value += 10
        return self.value
    
    def draw(self, canvas, pos):
# draw a hand on the canvas, use the draw method for cards
## assuming hand cards are horizontally placed
         first = pos[0]
         for card in self.cards:
            pos[0] =  first + CARD_SIZE[0] * self.cards.index(card) 
            card.draw(canvas, pos)
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
    
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)	# deal a card object from the deck
    
    def __str__(self):
        self.cardlist = "Deck contains:"
        for card in self.cards:
            self.cardlist +=  " "  + card.__str__()
        return self.cardlist



#define event handlers for buttons
def deal():     
    global outcome, action, in_play, deckcards, p_hand, d_hand, score 
    outcome = "                                      "
    if in_play:
        outcome = "Deal terminated, you lose."
        action  = "New deal?"
        score -= 1
        in_play = False     
    
    if not in_play:
        deckcards = Deck()
        deckcards.shuffle() 
        p_hand = Hand()  ##create new player hands
        d_hand = Hand()  ## create new dealer hands
        p_hand.add_card(deckcards.deal_card()) ##add two cards
        p_hand.add_card(deckcards.deal_card())
        print "Player " + p_hand.__str__() 
        d_hand.add_card(deckcards.deal_card())
        d_hand.add_card(deckcards.deal_card())
        print "Dealer " + d_hand.__str__()           
        in_play = True
        action  = "Hit or stand?"

def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global outcome, action, in_play, score
    if in_play:
        if p_hand.get_value() <= 21:
            p_hand.add_card(deckcards.deal_card())
            print "Player " + p_hand.__str__() 
            action = "Hit or stand?"
        if p_hand.get_value() > 21:
            outcome = "You have busted. Dealer WON!"
            score   -= 1   # hand lost game score -1
            in_play = False
            action  = "New deal?"
            print outcome
            

def stand():        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global outcome, action, in_play, score
    if in_play:
        while d_hand.get_value() < 17:
            d_hand.add_card(deckcards.deal_card())
            action = "Stand"
        print "Dealer " + d_hand.__str__() 
            
        if d_hand.get_value() > 21:
            outcome = "Dealer has busted."
            score += 1
            in_play = False
        else: 
            if d_hand.get_value() >= p_hand.get_value():
                outcome = "Dealer WON!"
                score -= 1
            else:
                outcome = "You WON!"
                score += 1
        action = "New deal?"        
        print outcome
        in_play = False
            
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play, score, outcome, action
    canvas.draw_text("Blackjack",(250,50), 34, "red")
    canvas.draw_text("Your Score: " + str(score), (420,80),24,"black")
    canvas.draw_text(outcome,(50,100),24, "black")
    canvas.draw_text(action, (300,140),24, "black")
    canvas.draw_text("Player", (100, 290),24,"black")
    canvas.draw_text("Dealer", (100, 140),24, "black") 
    p_hand.draw(canvas,[120, 300])
    d_hand.draw(canvas,[120, 150]) 
     
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (156,198),CARD_BACK_SIZE)
         
##    card = Card("S", "A")
##    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

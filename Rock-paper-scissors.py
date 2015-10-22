# Rock-paper-scissors-lizard-Spock miniproject
# made by j.z. on 10/13/2015


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
# helper functions

def name_to_number(name):
    if   (name == "rock"): number = 0
    elif (name == "Spock"): number =1
    elif (name == "paper"): number = 2
    elif (name == "lizard"): number = 3
    elif (name == "scissors"): number = 4
    else:
        print "input choice is out of scope"
    return number

def number_to_name(number):
    choice = ("rock","Spock","paper","lizard","scissors")
    name   = choice[number]
    if number <= 4: 
      return name
    else:
      return "input number " + str(number) + " is out of range"
        

def rpsls(player_choice): 
    #each choice wins against the preceding two choices and
    #loses aganist the following two cloclwise
    comp_number   = random.randrange(0,5)
    player_number = name_to_number(player_choice)
    comp_dif_player = comp_number - player_number
    comp_dif_player = comp_dif_player % 5 # result 1, 2, 3, 4
    if comp_dif_player == 0: 
       result = "Player and computer tie!\n"
    elif comp_dif_player <= 2:
       result = "Computer wins!\n"
    else:
       result = "Player wins!\n"
    print "Player chooses " + player_choice
    print "Computer chooses " + number_to_name(comp_number)
    return result
            
# test your code 
print rpsls("rock")
print rpsls("Spock")
print rpsls("paper")
print rpsls("lizard")
print rpsls("scissors")




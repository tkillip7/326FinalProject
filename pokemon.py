import re
from numpy import char

import pandas as pd

# So,
# We're going to have a 1v1 game, where player chooses a pokemon and computer
# chooses pokemon.

# When we run the program, it'll start like this (refer to turn methods):

# Hello Human!
# Please enter your name: (input)
# What's up (input)!

# Computer needs a name!
# Please enter Computer's name: (input)
# What's up (input).....
#
# Player 1, please choose a pokemon (give a list of names, if name )
#                                   (isn't valid, tell user to enter again)
#
# Based on the input, create a Pokemon object based on that
#
# What pokemon will Player 2 have?
# Based on the input, create a Pokemon object based on that
#
#
# The Pokemon have been selected!
# It's (Player 1's pokemon) vs (Player 2's pokemon)!
#
#
# Player 1, what move will you choose? Present the pokemon's movelist
# and have player 1 input what move they want, if playeer misspells or
# enters a wrong move, tell player that it's not a valid choice
#
# Player 2, what move will you choose? Same as player 1 instructions.
#
# Whichever pokemon is faster (compare speeds), they attack first
#
#
# Terminal will print, (Player's pokemon) used (move)! (Other player's pokemon)
# has (health) left!
#
# and then same for opposing pokemon, this continues until health is 0
#
#
# Here, we can just display a graph of some sort for pandas just for no reason
#
# Then ask user if he wants to reset, if "yes", then reset, else, say "goodbye"
#
#


class Pokemon:
    """ Initializes the 6 pokemon and their attributes.

    Attributes:
         health (int): health of the pokemon
         attack(str): the name of their attack
         defense (int): the defense effectiness
         damage (int): base damage of the pokemon
         type (str): the type of the pokemon
         speed (int): how fast the pokemon is

    """

    def __init__(self,health,attack,defense,type,speed,moves):
        
        self.health = health
        
        self.attack = attack 
        
        self.defense = defense 
        
   
        
        self.type = type
        
        self.speed = speed 
        
        self.moves = moves #this is a list
        
        
    
    def fight(self, pokemon2):
        
        print("Hello user!")



def main(player1, computer):
    "start game"
    "do something like game.play()"
    ""
    Venasaur = Pokemon(500,100,100,"Grass",10,{"Tackle","Razor Leaf",
                                                "Sludge Bomb","Petal Dance"})
    return Venasaur

#if __name__ == "__main__":
#    args = parse_args(sys.argv[1:])
#    main(args.file)

  # game.play()
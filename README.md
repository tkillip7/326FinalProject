# 326FinalProject
The purpose of this repository is to hold our teams final project, a pokemon game that primarily occurs within the terminal.

The user will be given an option on which Pokemon they want to use, while having each Pokemon's stats displayed. The computer will randomly select an opposing pokemon. Both the player and computer will be able to select moves until the HP(Health) of one of the pokemon reaches 0. After that, options to see more detailed stat information and comparisons, along with the ability to replay will be provided.

The files within our repository consist of pokemon.py, which contains our projects code and game.
Pokemon_Moves.csv contains the moves of each pokemon. It contains all the information on each move, such as which pokemon is allowed to use what, along with their type and damage.
Likewise, Pokemons.csv contains the Pokemon we plan to use, along with their stats that we read in

Our code can be run from the command line using 'pokemon.py'. From there the program will have instructions on what to do next.

The terminal doesn't display the plots created, so runnning it on Jupyter would be another method to fully see the graphs created.

pokemon.py = This file will be our main project. 
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
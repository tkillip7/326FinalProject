This repository is made to hold the semester python project created by: Vinny Tran, Guillermo Ortiz, 
Trinity Kiilip, and Daniel Gonzalez. (INST326 – 0101)

Our team name is Football, although we changed our project idea to a Pokémon player versus computer 
based game that takes place in the terminal.  

The user will be given an option on which Pokemon they want to use, while having each Pokemon's stats 
displayed. The computer will randomly select an opposing pokemon. Both the player and computer will 
be able to select moves until the HP(Health) of one of the pokemon reaches 0. After that, options to 
see more detailed stat information and comparisons, along with the ability to replay will be provided.

The files in our repository and the reason for their inclusion are as follows;

Pokemon_Moves.csv:  This CSV file hold the attributes of each move for each Pokémon we included.

Pokemons.csv:       This CSV file holds the attributes for each individual Pokémon we included.

Pokemon.py:         This file contains the actual python program.


To run the code, one you are in the same directory of where all the files are being kept, in the 
terminal insert and run “python pokemon.py” if on windows or “python3 pokemon.py” if on Mac. From 
there the program will have instructions on what to do next.

• Clear instructions on how to use your program and/or interpret the output of the program, as applicable
<<<< >>>>


The terminal doesn't display the plots created, so runnning it on Jupyter would be another method to 
fully see the graphs created.

• Attributions: 

Trinity: 

Daniel: In the fight method, Daniel took care of the regex that was used to take in the Pokemon_Moves.csv 
file and created nested dictionaries for each Pokémon. This allowed for easy access to each Pokémon’s each 
moves and the move’s values.  Daniel also wrote the statuses method and stall method. These methods were 
to help immerse to the player in hope that it feels like the computer is another player. The stall method 
uses the sleep() method from the time library[1].

Guillermo:

Vinny:


Reference:
1.	Time. Sleep() in python. (2018, April 10). GeeksforGeeks. https://www.geeksforgeeks.org/sleep-in-python/ 
2.	



This repository is made to hold the semester python project created by: Vinny Tran, Guillermo Ortiz, Trinity Kiilip, and Daniel Gonzalez. (INST326 – 0101)

Our team’s name is Football, although we changed our project idea to a Pokémon player versus computer based game that takes place in the terminal.  

The user will be given an option on which Pokémon they want to use, while having each Pokémon’s stats displayed. The computer will randomly select an opposing Pokémon. Both the player and computer will be able to select moves until the HP(Health) of one of the Pokémon reaches 0. After that, options to 
see more detailed stat information and comparisons, along with the ability to replay will be provided.

The files in our repository and the reason for their inclusion are as follows;

Pokemon_Moves.csv: This CSV file hold the attributes of each move for each Pokémon we included.

Pokemons.csv: This CSV file holds the attributes for each individual Pokémon we included.

Pokemon.py: This file contains the actual python program.


To run the code, one you are in the same directory of where all the files are being kept, in the 
terminal insert and run “python pokemon.py” if on windows or “python3 pokemon.py” if on Mac. From there the program will have instructions on what to do next.

Some terms to look out for!
1.	HP: health points. 
2.	ATK: attack points.
3.	SPE: the Pokémon’s speed points.
4.	DEF: the Pokémon’s defense points. 
Lastly, terms such as Grass, Poison, Water, or Flying refer to the Pokémon’s abilities or nature in terms of their abilities. 

The terminal doesn't display the plots created, so running it on Jupyter would be another method to fully see the graphs created.

• Attributions: 

Trinity: Created the initial skeleton to get us started. Used pandas filtering to initialize the Pokémon object based on the two spreadsheets we used. I turned them into different data frames and filtered the Pokemon_Moves to gather a list of moves that only belongs to a certain Pokémon, which was determined with Dex_ID. Designed how we were going to create our Pokémon objects and helped design how the Pokémon battles will go. Added some user error prevention. Coded most of the code in main. Also created the str magic method so we can print the Pokémon object and display each Pokémon’s stats. 

Daniel: In the fight method, Daniel created the regular expression that was used to take in the Pokemon_Moves.csv file and created nested dictionaries for each Pokémon. This allowed for easy access to each Pokémon’s each moves and the move’s values. I then implemented each captured group throughout the fight method. Daniel also wrote the statuses method and stall method. These methods were to help immerse to the player in hope that it feels like the computer is another player. The stall method uses the sleep() method from the time library[1]. These methods were used throughout pokemon.py. 

Guillermo: Created the compare method used to see information regarding the Pokémon moves and stats. Created the data visualizations using both csv files and pandas/matplotlib. This method was used to allow players a closer look at move stats, and a direct comparison for each of the Pokémon’s stat attributes. 

Vinny: In the compare() method, Vinny helped with reading the csv. files while also working on some of the pandas. This helped in comparing 2 Pokémon side-by-side. In if name == "main", Vinny made the replay prompt, looping users to input a correct answer of yes and no. In this function, when replay is true, the Pokémon object's health will be reset when battling again. If replay is false, the project will end. Vinny made Pokemon_Moves.csv and Pokemons.csv files for pandas. Made console edits to make the project simulate like a real Pokémon battle.

Reference:
1.	Time. Sleep() in python. (2018, April 10). GeeksforGeeks. https://www.geeksforgeeks.org/sleep-in-python/ 
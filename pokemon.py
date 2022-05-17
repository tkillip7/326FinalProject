import re
import random
from numpy import char
import pandas as pd
from time import sleep
import matplotlib.pyplot as plt


class Pokemon:
    """Creates pokemon objects. Also starts the Pokemon battle between the 
    player and the computer.

    Our project aims to provide our user with a working battle simulation that 
    mimics that of Pokemon. 
    The objective of the game is to choose 1 Pokemon out of the 3 given and 
    battle with the opponent. 
    Each user will use a Pokemon’s given moveset of 4 moves to battle with the 
    opponent, dealing damage over time with a move. 
    The winner is decided if the opponent’s Pokemon’s HP (Health Points) drops 
    down to 0. 
    At the end of each turn, it will display each Pokemon’s remaining HP.
    """
    #Primary Author for Pokemon_Moves.csv and Pokemons.csv: Vinny

    def __init__(self, name, dex_id, type1, type2, hp, atk, defence, spe): #Primary Author(s): Trinity
        """Creates dataframe from csv files. Filters it to find information
        regarding the pokemon along with their moves

        Args:
            name (string): string name of the pokemon read from csv
            dex_id (int): pokedex number for each pokemon
            type1 (string): string of the first type for each pokemon
            type2 (string): string of pokemons second type if applicable
            hp (int): int health value for each pokemon
            atk (int): int attack value for each pokemon
            defence (int): defense value for each pokemon
            spe (int): speed value for each of the pokemon
        """
        self.name = name
        self.dex_id = dex_id
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.spe = spe

        df_2 = pd.read_csv("Pokemons.csv")
        df = pd.read_csv("Pokemon_Moves.csv")

        if (name == "Venasaur"):
            filter = df["Dex_ID"] == 3
            v_moves_filter = df[filter]
            venasaur_moves = v_moves_filter["Move_Name"].tolist()
            self.moves = venasaur_moves

        elif (name == "Charizard"):
            filter = df["Dex_ID"] == 6
            c_moves_filter = df[filter]
            charizard_moves = c_moves_filter["Move_Name"].tolist()
            self.moves = charizard_moves

        elif (name == "Blastoise"):
            filter = df["Dex_ID"] == 9
            b_moves_filter = df[filter]
            blastoise_moves = b_moves_filter["Move_Name"].tolist()
            self.moves = blastoise_moves

    def __str__(self): #Primary Author(s): Trinity
        """Converts Pokemon class object into a string, then returns it

        Returns:
            _type_: Returns pokemon object as a string, containing all stats
            along with typing
        """
        return f"{self.name}, {self.type1}, {self.type2}, HP: {self.hp}, ATK: {self.atk}, SPE: {self.spe}, DEF: {self.defence}"

    def fight(self, Pokemon1, Pokemon2): #Primary Author(s):Daniel, Trinity 
        """Main fight function, finishes move creation and checks to see
        which Pokemon goes first to attack. Afterwards, player and computer
        choose moves until the HP of 1 Pokemon hits 0.

        Args:
            Pokemon1 (str): Pokemon chosen by the player
            Pokemon2 (str): Pokemon chosen by the computer

        Raises:
            ValueError: Raises value error if string was unable to be parsed 
            through using Regex

         Side Effects:
            Prints the available move choices for the chosen Pokemon and the 
            Turn order
        """    
        regex = (r"""(?xm)
                ^
                (?P<dex_Id>[\d+])
                , 
                (?P<move_name>[\w]+?[ \w]+)
                ,
                (?P<type>[\w]+)
                ,
                (?P<power>[\d]+)
                ,
                (?P<accuracy>[\d]+)""")
        r = "Pokemon_Moves.csv"
        new_list = []
        with open(r, "r", encoding="utf-8") as f:   
            new_list = [(line.strip("\n")) for line in f]
        new_list.remove("Dex_ID,Move_Name,Type,Power,Accuracy")
        
        dict_3 = {}
        dict_6 = {}
        dict_9 = {}

        for i in new_list:
            moves_attributes = re.search(regex, i)
            
            if  moves_attributes == None:
                    raise ValueError("The string could not be matched.")
            else:
                dex_id = int(moves_attributes.group(1))
                move = (moves_attributes.group(2)).lower()
                type = (moves_attributes.group(3)).lower()
                power = int(moves_attributes.group(4))
                accuracy = int(moves_attributes.group(5))
                
                if dex_id == 3:
                    dict_3[f"{move}"] = (type,power,accuracy)
                elif dex_id == 6:
                    dict_6[f"{move}"] = (type,power,accuracy)
                elif dex_id == 9:
                    dict_9[f"{move}"] = (type,power,accuracy)
                    
        moves_dict = {3:dict_3, 6:dict_6, 9:dict_9}
        turns = 1
        next_turn = 0
        while Pokemon1.hp >= 1 and Pokemon2.hp >=1:
            #first turn conditions
            if turns == 1:
                if Pokemon1.spe > Pokemon2.spe:
                    print(f"Turn {turns}!")
                    print(f"{Pokemon1.name} goes first! pick a move: {Pokemon1.moves}")
                    move = (input("Type the move: ")).lower()
                    
                    damage = ((moves_dict[self.dex_id])[move])[1]
                    pokemon2.hp -= damage
                    
                    next_turn = 2
                    turns += 1
                    self.statuses()
                    self.compare()
                else:
                    print(f"Turn {turns}!")
                    print(f"{Pokemon2.name} goes first!")
                    self.stall(.5)
                    choice = (str(random.choice(list(moves_dict[pokemon2.dex_id])))).lower()
                     
                    print(f"{Pokemon2.name} chose {choice}!")
                    damage = ((moves_dict[pokemon2.dex_id])[choice])[1]
                    pokemon1.hp -= damage
                    
                    next_turn = 1
                    turns += 1
                    self.statuses()   
                    self.compare()
                    
            #all proceeding turn conditions        
            if next_turn == 1:
                print(f"Turn {turns}!")
                print(f"{Pokemon1.name}'s turn! pick a move: {Pokemon1.moves}")
                move = (input("Type the move: ")).lower()
                
                damage = ((moves_dict[self.dex_id])[move])[1]
                pokemon2.hp -= damage
                
                next_turn = 2
                turns += 1
                
                self.statuses()  
                self.compare()
                
            elif next_turn == 2:
                print(f"Turn {turns}!")
                print(f"{Pokemon2.name}'s turn!")
                choice = (str(random.choice(list(moves_dict[Pokemon2.dex_id])))).lower()
                
                self.stall(.50)
                
                print(f"{Pokemon2.name} chooses {choice}!")
                damage = ((moves_dict[Pokemon2.dex_id])[str(choice)])[1]
                pokemon1.hp -= damage
                
                turns += 1
                next_turn = 1

                self.statuses()   
                self.compare()
         
            
    def statuses(self): #Primary Author(s): Daniel
        """Reads the Pokemon to detect what HP (HealthPoints) a Pokemon 
        currently has. At the end of every turn, it will display the HP of each 
        Pokemon. If any of the pokemon have HP that is less than 0, it will end the 
        battle and print the winner. 

        Side Effects:
            Prints the victory or loss statement and Prints the HP of each Pokemon.
        """
        if pokemon1.hp <= 0:
            print("Oh no!")
            self.stall(int(1))
            print(f"{pokemon1.name} Fainted! \n\n the player lost! \n\n")
            return print("Better luck next time...")
        elif pokemon2.hp <= 0:
            print("Oh wait!")
            self.stall(int(1))
            print(f"{pokemon2.name} Fainted! \n\n \n    You win! \n\n")
            return  print("Till next time!...")
        else:
            print(f"{pokemon1.name}'s HP is: {pokemon1.hp}\n{pokemon2.name}'s HP is: {pokemon2.hp}")
            print("---------------------------------------------------------")
               

    def stall(self, num = 1, dots = 4): #Primary Author(s): Daniel
        """Used to imitate time passing. Mimics what it might look like when 
        a player is making a decision

        Args:
            num (int, optional): Number of seconds to stall. Defaults to 1.
            dots (int, optional): Number of dots to print. Defaults to 4.
        Side Effects:
            prints to terminal.
        """


        while dots !=0:
            sleep(num) #in seconds
            print('.')
            dots -= 1

    def compare(self): #Primary Author(s): Guillermo | Secondary Author(s):Vinny
        """Reads csv files on pokemon stats and moves. Asks user if they want
        to see a visual of these stats.
        
        
        Side Effects:
            Prints question with user input along with plots and data read
            from the Pokemon and Pokemon moves csv.
        """        
        if pokemon1.hp <=0 or pokemon2.hp <=0:
            df2 = pd.read_csv("Pokemon_Moves.csv")
            stats = pd.read_csv("Pokemons.csv")
            display_question = (input("""\n
Would you like to see each Pokemon's stats and moves?
If so enter Yes, if not enter No.\n""")).lower()
            if display_question == 'yes':
                hp_display = stats.plot.bar(x = "Name", y = "HP")
                atk_display =stats.plot.bar(x = "Name", y = "Atk")
                def_display = stats.plot.bar(x = "Name", y = "Def")
                spe_display = stats.plot.bar(x = "Name", y = "Spe")
                print ("Here are the HP values", hp_display)
                print ("Here are the Atk values", atk_display)
                print ("Here are the Def values", def_display)
                print ("Here are the Speed values", spe_display)
                print ("\nVenasaur's data:\n" ,df2.loc[[0,1,2,3]])
                print ("\nCharizard's data: \n",df2.loc[[4,5,6,7]])
                print ("\nBlastoise's data: \n",df2.loc[[8,9,10,11]])
            elif display_question == 'no':
                pass
            else:
                raise ValueError("\nPlease enter 'Yes or 'No\n")
           

if __name__ == "__main__": #Primary Author(s): Vinny | 
    #Secondary Author(s): Guillermo
    
    """Runs the fight. 
    Gives user input for Pokemon choice. 
    Gives user input to replay the fight

     Side Effects:
            Prints the introduction of the game and user input directions such 
            as Pokemon choice and if they want to fight again.
    """

    replay = True
    while replay:
        # Create an object for each pokemon
        venasaur = Pokemon("Venasaur", 3, "Grass", "Poison", 800, 82, 83, 80)
        charizard = Pokemon("Charizard", 6, "Fire", "Flying", 780, 84, 78, 100)
        blastoise = Pokemon("Blastoise", 9, "Water", "N/A", 790, 83, 100, 78)

        lst = [venasaur.name,charizard.name,blastoise.name]
        first,second,third = lst

        # Making sure the user inputs a valid option

    
        choice = False
        while choice == False:
            print("\nHello Player!")
            print("---------------------------------------------------------")
            print(f"Which pokemon do you want to use? Here are the stats")
            print("---------------------------------------------------------")
            print(venasaur)
            print(charizard)
            print(blastoise)
            print("---------------------------------------------------------")
            print(f"{first}, {second}, {third} or compare pokemon")
            p_choice = int(input("\nUse 0 , 1, or 2 to choose respectively:"))
            if p_choice < 0 or p_choice > 2:
                print("This isn't a valid choice!")
            else:
                if p_choice == 0:
                    pokemon1 = venasaur
                elif p_choice == 1:
                    pokemon1 = charizard
                elif p_choice == 2:
                    pokemon1 = blastoise
                print(f"You chose {pokemon1.name}!")

                choice = True

        # computer
        c_choice = random.randrange(3)
        if c_choice == p_choice:
            while c_choice == p_choice:
                c_choice = random.randrange(3)
        if c_choice == 0:
            pokemon2 = venasaur
        elif c_choice == 1:
            pokemon2 = charizard
        elif c_choice == 2:
            pokemon2 = blastoise
        Pokemon.stall(Pokemon,.75)
        print(f"Your opponent chose {pokemon2.name}!")
        Pokemon.stall(Pokemon,.75)

        # the battle begins!
        # fastest pokemon goes first

        pokemon1.fight(pokemon1,pokemon2)
        
        valid = False
        while not valid:
            r_choice = (input("Do you want to fight again? (Yes/No)\n\n")).lower()
            if r_choice == "no":
                replay = False
                valid = True
                print("\nThanks for playing!")
            if r_choice == "yes":
                replay = True
                valid = True
                print("\nLets go!")




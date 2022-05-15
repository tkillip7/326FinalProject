import re
import random
from numpy import char
import pandas as pd
from time import sleep
import matplotlib.pyplot as plt


class Pokemon:
    """_summary_
    """

    def __init__(self, name, dex_id, type1, type2, hp, atk, defence, spe):
        """_summary_

        Args:
            name (_type_): _description_
            dex_id (_type_): _description_
            type1 (_type_): _description_
            type2 (_type_): _description_
            hp (_type_): _description_
            atk (_type_): _description_
            defence (_type_): _description_
            spe (_type_): _description_
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

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"{self.name}, {self.type1}, {self.type2}, HP: {self.hp}, ATK: {self.atk}, SPE: {self.spe}, DEF: {self.defence}"

    def fight(self, Pokemon1, Pokemon2):
        
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
                    raise ValueError("The address string could not be parsed.")
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
                    print(f"{Pokemon1.name} goes first! pick a move: {Pokemon1.moves}")
                    move = (input("Type the move: ")).lower()
                    
                    damage = ((moves_dict[self.dex_id])[move])[1]
                    pokemon2.hp -= damage
                    
                    next_turn = 2
                    turns += 1
                    
                    self.stall(int(.5))
                    print(f"Turn {turns}!")
                    self.statuses()
                    self.compare()
                else:
                    print(f"{Pokemon2.name} goes first!")
                    self.stall(int(.5))
                    choice = (str(random.choice(list(moves_dict[pokemon2.dex_id])))).lower()
                    
                    print(f"{Pokemon2.name} chose {choice}!")
                    damage = ((moves_dict[pokemon2.dex_id])[choice])[1]
                    pokemon1.hp -= damage
                    
                    next_turn = 1
                    turns += 1
                    
                    self.stall(int(.5))
                    print(f"Turn {turns}!")
                    self.statuses()   
                    self.compare()
                    
            #all proceeding turn conditions        
            if next_turn == 1:
                
                print(f"{Pokemon1.name}'s turn! pick a move: {Pokemon1.moves}")
                move = (input("Type the move: ")).lower()
                
                damage = ((moves_dict[self.dex_id])[move])[1]
                pokemon2.hp -= damage
                
                next_turn = 2
                turns += 1
                
                self.stall(int(.15))
                print(f"Turn {turns}!")
                self.statuses()  
                self.compare()
                
            elif next_turn == 2:
                
                print(f"{Pokemon2.name}'s turn!")
                choice = (str(random.choice(list(moves_dict[Pokemon2.dex_id])))).lower()
                
                self.stall(int(.5))
                
                print(f"{Pokemon2.name} chooses {choice}!")
                damage = ((moves_dict[Pokemon2.dex_id])[str(choice)])[1]
                pokemon1.hp -= damage
                
                turns += 1
                next_turn = 1
                
                self.stall(int(.15))
                print(f"Turn {turns}!")
                self.statuses()   
                self.compare()
         
            
    def statuses(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if pokemon1.hp <= 0:
            print("Oh no!")
            self.stall(int(.5))
            print(f"{pokemon1.name} Fainted! \n\n the player lost! \n\n")
            return print("Better luck next time...")
        elif pokemon2.hp <= 0:
            print("Oh wait!")
            self.stall(int(.5))
            print(f"{pokemon2.name} Fainted! \n\n \n    You win! \n\n")
            return  print("Till next time!...")
        else:
            print(f"{pokemon1.name}'s HP is: {pokemon1.hp}\n{pokemon2.name}'s HP is: {pokemon2.hp}")
            print("---------------------------------------------------------")
               

    def stall(delay = 1, dots = 4): #this is to create the feeling of facing an actual player. A slight wait inbetween turns/decisions.
        """_summary_

        Args:
            delay (int, optional): _description_. Defaults to 1.
            dots (int, optional): _description_. Defaults to 4.
        """

        while dots !=0:
            sleep(int(delay)) #in seconds
            print('.')
            dots -= 1
    def compare(self):
        if pokemon1.hp <=0 or pokemon2.hp <=0:
            df = pd.read_csv("Pokemons.csv")
            df2 = pd.read_csv("Pokemon_Moves.csv")
            stats = pd.read_csv("Pokemons.csv")
            display_question = input("""Would you like to see each Pokemon's
stats and moves? 
If so enter Yes, if not enter No \n""")
            if display_question == 'Yes':
                hp_display = stats.plot.bar(x = "Name", y = "HP")
                atk_display =stats.plot.bar(x = "Name", y = "Atk")
                def_display = stats.plot.bar(x = "Name", y = "Def")
                spe_display = stats.plot.bar(x = "Name", y = "Spe")
                print ("Here are the HP values", hp_display)
                print ("Here are the Atk values", atk_display)
                print ("Here are the Def values", def_display)
                print ("Here are the Speed values", spe_display)
                print ("Venasaur's data:\n" ,df2.loc[[0,1,2,3]])
                print ("Charizard's data: \n",df2.loc[[4,5,6,7]])
                print ("Blastoise's data: \n",df2.loc[[8,9,10,11]])
            elif display_question == 'No':
                pass
            else:
                raise ValueError("Please enter 'Yes or 'No")
           
if __name__ == "__main__":

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
            print(f"{first}, {second}, {third}")
            p_choice = int(input("\nUse 0 , 1, or 2 to choose respectively: "))
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
        Pokemon.stall()
        print(f"Your opponent chose {pokemon2.name}!")
        Pokemon.stall(.10,3)

        # the battle begins!
        # fastest pokemon goes first

        pokemon1.fight(pokemon1,pokemon2)

        valid = False
        while not valid:
            r_choice = input("Do you want to fight again? (Yes/No)\n\n").lower()
            if r_choice == "no":
                replay = False
                valid = True
            else:
                valid = True
            





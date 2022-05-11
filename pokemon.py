import re
import random
from numpy import char
import pandas as pd
from time import sleep

class Pokemon:

    def __init__(self, name, dex_id, type1, type2, hp, atk, defence, spe):
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

    def computer(self, Pokemon2, move):
        
        if move == "Tackle":
            Pokemon2.hp -= 40
        elif move == "Razor Leaf":
            Pokemon2.hp -= 55
        elif move == "Sludge Bomb":
            Pokemon2.hp -= 90
        elif move == "Petal Dance":
            Pokemon2.hp -= 120
        elif move == "Flamethrower":
            Pokemon2.hp -= 90
        elif move == "Air Slash":
            Pokemon2.hp -= 75
        elif move == "Seismic Toss":
            Pokemon2.hp -= 60
        elif move == "Slash":
            Pokemon2.hp -= 70
        elif move == "Rapid Spin":
            Pokemon2.hp -= 50
        elif move == "Ice Beam":
            Pokemon2.hp -= 90
        elif move == "Hydro Pump":
            Pokemon2.hp -= 110
        elif move == "Aqua Tail":
            Pokemon2.hp -= 90

    def fight(self, Pokemon1, Pokemon2):
        # Start of game
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
            #first round conditions
            if turns == 1:
                if Pokemon1.spe > Pokemon2.spe:
                    print(f"{Pokemon1.name} goes first! pick a move: {Pokemon1.moves}")
                    move = (input("Type the move: ")).lower()
                    
                    damage = ((moves_dict[self.dex_id])[move])[1]
                    pokemon2.hp -= damage
                    
                    turns += 1
                    Pokemon.statuses()
                    next_turn = 2
                    stall(.15,3)
                    print(f"Round {turns}!")
                else:
                    print(f"{Pokemon2.name} goes first!")
                    stall()
                    choice = (str(random.choice(list(moves_dict[self.dex_id])))).lower()
                    
                    print(f"{Pokemon2.name} chose {choice}!")
                    damage = ((moves_dict[pokemon2.dex_id])[choice])[1]
                    pokemon1.hp -= damage
                    
                    turns += 1
                    Pokemon.statuses()
                    next_turn = 1
                    stall(.15,3)
                    print(f"Round {turns}!")
                    
            #all proceeding round conditions        
            if next_turn == 1:
                
                print(f"{Pokemon1.name}'s turn! pick a move: {Pokemon1.moves}")
                move = (input("Type the move: ")).lower()
                
                damage = ((moves_dict[self.dex_id])[move])[1]
                pokemon2.hp -= damage
                
                turns += 1
                Pokemon.statuses()
                next_turn = 2
                stall(.15,3)
                print(f"Round {turns}!")
                
            elif next_turn == 2:
                
                print(f"{Pokemon2.name}'s turn!")
                choice = (str(random.choice(list(moves_dict[self.dex_id])))).lower()
                
                stall()
                
                print(f"{Pokemon2.name} chooses {choice}!")
                damage = ((moves_dict[pokemon2.dex_id])[str(choice)])[1]
                pokemon1.hp -= damage
                
                turns += 1
                Pokemon.statuses()
                next_turn = 1
                stall(.15,3)
                print(f"Round {turns}!")   
                 
    def statuses():
        print(f"{pokemon1.name}'s hp is: {pokemon1.hp} and {pokemon2.name}'s hp is: {pokemon2.hp} \n")   

def stall(delay = .5, dots = 4): #this is to create the feeling of facing an actual player. A slight wait inbetween turns/decisions.

    while dots !=0:
        sleep(delay) #in seconds
        print('.')
        dots -= 1
            
# Create an object for each pokemon
venasaur = Pokemon("Venasaur", 3, "Grass", "Poison", 800, 82, 83, 80)
charizard = Pokemon("Charizard", 6, "Fire", "Flying", 780, 84, 78, 100)
blastoise = Pokemon("Blastoise", 9, "Water", "N/A", 790, 83, 100, 78)

lst = [venasaur.name,charizard.name,blastoise.name]
first,second,third = lst

# Making sure the user inputs a valid option
choice = False
while choice == False:
    print("Hello Player!")
    print(f"Which pokemon do you want to use?")
    print(f"{first}, {second}, {third}")
    p_choice = int(input("Use 0 , 1, or 2 to choose: "))
    if p_choice < 0 or p_choice > 2:
        print("this isn't a valid choice!")
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

if c_choice == 0:
    pokemon2 = venasaur
elif c_choice == 1:
    pokemon2 = charizard
elif c_choice == 2:
    pokemon2 = blastoise
stall()
print(f"Your opponent choose {pokemon2.name}!")
stall(.10,3)

# the battle begins!
# fastest pokemon goes first

pokemon1.fight(pokemon1,pokemon2)



print("done!")

import re
import random
from numpy import char
import pandas as pd


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

        df_2 = pd.read_csv("Pokemon (4).csv")
        df = pd.read_csv("Pokemon_Moves (1).csv")

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
            filter = df["Dex_ID"] == 3
            b_moves_filter = df[filter]
            blastoise_moves = b_moves_filter["Move_Name"].tolist()
            self.moves = blastoise_moves

    def attack(self, Pokemon2, move):

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

      while Pokemon1.hp > 0 or Pokemon2.hp > 0:
        # faster pokemon goes first
        if Pokemon1.hp <= 0:
                print(f"{Pokemon1.name} has fainted!")
                break
        elif Pokemon2.hp <= 0:
                print(f"{Pokemon2.name} has fainted!")
                break
            
        if Pokemon1.spe > Pokemon2.spe:
            # Pokemon 1's turn
            print(f"{Pokemon1.name}'s turn! Choose a move! {Pokemon1.moves}")
            move = input("Type the move: ")
            if move == "Tackle":
                Pokemon1.attack(Pokemon2, "Tackle")
                print(f"{Pokemon1.name} used tackle!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Razor Leaf":
                Pokemon1.attack(Pokemon2, "Razor Leaf")
                print(f"{Pokemon1.name} used Razor Leaf!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Sludge Bomb":
                Pokemon1.attack(Pokemon2, "Sludge Bomb")
                print(f"{Pokemon1.name} used Sludge Bomb!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Petal Dance":
                Pokemon1.attack(Pokemon2, "Petal Dance")
                print(f"{Pokemon1.name} used Petal Dance!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Flamethrower":
                Pokemon1.attack(Pokemon2, "Flamethrower")
                print(f"{Pokemon1.name} used Flamethrower!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Air Slash":
                Pokemon1.attack(Pokemon2, "Air Slash")
                print(f"{Pokemon1.name} used Air Slash!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Seismic Toss":
                Pokemon1.attack(Pokemon2, "Seismic Toss")
                print(f"{Pokemon1.name} used Seismic Toss!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Slash":
                Pokemon1.attack(Pokemon2, "Slash")
                print(f"{Pokemon1.name} used Slash!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Rapid Spin":
                Pokemon1.attack(Pokemon2, "Rapid Spin")
                print(f"{Pokemon1.name} used Rapid Spin!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Ice Beam":
                Pokemon1.attack(Pokemon2, "Ice Beam")
                print(f"{Pokemon1.name} used Ice Beam!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Hydro Pump":
                Pokemon1.attack(Pokemon2, "Hydro Pump")
                print(f"{Pokemon1.name} used Hydro Pump!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Aqua Tail":
                Pokemon1.attack(Pokemon2, "Aqua Tail")
                print(f"{Pokemon1.name} used Aqua Tail!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            

            # Pokemon 2's Turn!
            all_moves = ["Tackle", "Razor Leaf", "Sludge Bomb", "Petal Dance",
                             "Flamethrower", "Air Slash", "Seismic Toss", "Slash",
                             "Rapid Spin", "Ice Beam", "Hydro Pump", "Aqua Tail"]
            
            

            print(f"{Pokemon2.name}'s turn!")

            opp = random.choice(all_moves)
            print(opp)
            if opp == "Tackle":
                Pokemon2.attack(Pokemon1, "Tackle")
                print(f"{Pokemon2.name} used Tackle!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Razor Leaf":
                Pokemon2.attack(Pokemon1, "Razor Leaf")
                print(f"{Pokemon2.name} used Razor Leaf!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Sludge Bomb":
                Pokemon2.attack(Pokemon1, "Sludge Bomb")
                print(f"{Pokemon2.name} used Sludge Bomb!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Flamethrower":
                Pokemon2.attack(Pokemon1, "Flamethrower")
                print(f"{Pokemon2.name} used Flamethrower!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Air Slash":
                Pokemon2.attack(Pokemon1, "Air Slash")
                print(f"{Pokemon2.name} used Air Slash!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Seismic Toss":
                Pokemon2.attack(Pokemon1, "Seismic Toss")
                print(f"{Pokemon2.name} used Seismic Toss!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Slash":
                Pokemon2.attack(Pokemon1, "Slash")
                print(f"{Pokemon2.name} used Slash!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Ice Beam":
                Pokemon2.attack(Pokemon1, "Ice Beam")
                print(f"{Pokemon2.name} used Ice Beam!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Hydro Pump":
                Pokemon2.attack(Pokemon1, "Hydro Pump")
                print(f"{Pokemon2.name} used Hydro Pump!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
            elif opp == "Aqua Tail":
                Pokemon2.attack(Pokemon1, "Aqua Tail")
                print(f"{Pokemon2.name} used Aqua Tail!")
                print(f"{Pokemon1.name} has {Pokemon1.hp} hp left")
                
            
        
      

            
                
        else:
            
             # Pokemon 2's Turn!
            all_moves = ["Tackle", "Razor Leaf", "Sludge Bomb", "Petal Dance",
                             "Flamethrower", "Air Slash", "Seismic Toss", "Slash",
                             "Rapid Spin", "Ice Beam", "Hydro Pump", "Aqua Tail"]

            print(f"{Pokemon2.name}'s turn!")
            
            opp = random.choice(all_moves)
            
            if opp == "Tackle":
                Pokemon2.attack(Pokemon1,"Tackle")
                print(f"{Pokemon2.name} used Tackle!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Razor Leaf":
                Pokemon2.attack(Pokemon1,"Razor Leaf")
                print(f"{Pokemon2.name} used Razor Leaf!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Sludge Bomb":
                Pokemon2.attack(Pokemon1,"Sludge Bomb")
                print(f"{Pokemon2.name} used Sludge Bomb!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Flamethrower":
                Pokemon2.attack(Pokemon1,"Flamethrower")
                print(f"{Pokemon2.name} used Flamethrower!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Air Slash":
                Pokemon2.attack(Pokemon1,"Air Slash")
                print(f"{Pokemon2.name} used Air Slash!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Seismic Toss":
                Pokemon2.attack(Pokemon1,"Seismic Toss")
                print(f"{Pokemon2.name} used Seismic Toss!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Slash":
                Pokemon2.attack(Pokemon1,"Slash")
                print(f"{Pokemon2.name} used Slash!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Ice Beam":
                Pokemon2.attack(Pokemon1,"Ice Beam")
                print(f"{Pokemon2.name} used Ice Beam!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Hydro Pump":
                Pokemon2.attack(Pokemon1,"Hydro Pump")
                print(f"{Pokemon2.name} used Hydro Pump!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif opp == "Aqua Tail":
                Pokemon2.attack(Pokemon1,"Aqua Tail")
                print(f"{Pokemon2.name} used Aqua Tail!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            
            # Pokemon 1's turn
            print(f"{Pokemon1.name}'s turn! Choose a move! {Pokemon1.moves}")
            move = input("Type the move: ")
            if move == "Tackle":
                Pokemon1.attack(Pokemon2,"Tackle")
                print(f"{Pokemon1.name} used tackle!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Razor Leaf":
                Pokemon1.attack(Pokemon2,"Razor Leaf")
                print(f"{Pokemon1.name} used Razor Leaf!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Sludge Bomb":
                Pokemon1.attack(Pokemon2,"Sludge Bomb")
                print(f"{Pokemon1.name} used Sludge Bomb!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Petal Dance":
                Pokemon1.attack(Pokemon2,"Petal Dance")
                print(f"{Pokemon1.name} used Petal Dance!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Flamethrower":
                Pokemon1.attack(Pokemon2,"Flamethrower")
                print(f"{Pokemon1.name} used Flamethrower!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Air Slash":
                Pokemon1.attack(Pokemon2,"Air Slash")
                print(f"{Pokemon1.name} used Air Slash!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Seismic Toss":
                Pokemon1.attack(Pokemon2,"Seismic Toss")
                print(f"{Pokemon1.name} used Seismic Toss!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Slash":
                Pokemon1.attack(Pokemon2,"Slash")
                print(f"{Pokemon1.name} used Slash!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Rapid Spin":
                Pokemon1.attack(Pokemon2,"Rapid Spin")
                print(f"{Pokemon1.name} used Rapid Spin!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Ice Beam":
                Pokemon1.attack(Pokemon2,"Ice Beam")
                print(f"{Pokemon1.name} used Ice Beam!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Hydro Pump":
                Pokemon1.attack(Pokemon2,"Hydro Pump")
                print(f"{Pokemon1.name} used Hydro Pump!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
            elif move == "Aqua Tail":
                Pokemon1.attack(Pokemon2,"Aqua Tail")
                print(f"{Pokemon1.name} used Aqua Tail!")
                print(f"{Pokemon2.name} has {Pokemon2.hp} hp left")
        
            if Pokemon1.hp <= 0:
                print(f"{Pokemon1.name} fainted!")
                break
            elif Pokemon2.hp <= 0:
                print(f"{Pokemon2.name} fainted")
                break
            
            

       

regex = (r"""(?xm)
        ^\w+:\s
        (?P<Pokemon_name>[\w]+)
        ,\s\w+:\s
        (?P<Dex_id>[\d]+)
        ,\s\w+:\s
        (?P<Type1>[\w]+)
        ,\s\w+:\s
        (?P<Type2>[\w]+)
        ,\s\w+:\s
        (?P<Hp>[\d]+)
        ,\s\w+:\s
        (?P<Atk>[\d]+)
        ,\s\w+:\s
        (?P<Def>[\d]+)
        ,\s\w+:\s
        (?P<Spe>[\d]+)""")

# pokemon file is read
r = "Pokemon_list.txt"
new_list = []
with open(r, "r", encoding="utf-8") as f:
    new_list = [(line.strip('\n')) for line in f]




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
    print(f"{first},{second},{third}")
    p_choice = int(input("Use 0,1,or 2 to choose"))
    if p_choice < 0 or p_choice > 2:
        print("this isn't a valid choice!")
    else:
        choice = True



if p_choice == 0:
    pokemon1 = venasaur
elif p_choice == 1:
    pokemon1 = charizard
elif p_choice == 2:
    pokemon1 = blastoise

print(f"You chose {pokemon1.name}!")


# computer

c_choice = random.randrange(3)

if c_choice == 0:
    pokemon2 = venasaur
elif c_choice == 1:
    pokemon2 = charizard
elif c_choice == 2:
    pokemon2 = blastoise

print(f"You are facing {pokemon2.name}!")

# the battle begins!
# fastest pokemon goes first

pokemon1.fight(pokemon1,pokemon2)



match = re.search(regex, str(new_list[p_choice]))

pokemon_attributes = re.search(regex, str(new_list[p_choice]))

# assignments are made
pokemon_p = pokemon_attributes.group(0)

pokemon_name = pokemon_attributes.group(1)

dex_id = pokemon_attributes.group(2)

type1 = pokemon_attributes.group(3)

type2 = pokemon_attributes.group(4)

hp = pokemon_attributes.group(5)

attack = pokemon_attributes.group(6)

defense = pokemon_attributes.group(7)

speed = pokemon_attributes.group(8)

# ---------------------

# computer's choosen pokemon

match = re.search(regex, str(new_list[c_choice]))

pokemon_attributes = re.search(regex, str(new_list[c_choice]))

pokemon_c = pokemon_attributes.group(0)

pokemon_name = pokemon_attributes.group(1)

dex_id = pokemon_attributes.group(2)

type1 = pokemon_attributes.group(3)

type2 = pokemon_attributes.group(4)

hp = pokemon_attributes.group(5)

attack = pokemon_attributes.group(6)

defense = pokemon_attributes.group(7)

speed = pokemon_attributes.group(8)

# test to see which pokemon was choosen
print("stats!")
print(pokemon_p)
print(pokemon_c)
print(pokemon_attributes)

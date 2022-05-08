import re
import random
from numpy import char
import pandas as pd

class Pokemon:
    
    def __init__(self,name,dex_id,type1,type2,hp,atk,defence,spe):
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
        
    def attack(self,Pokemon2,move):
        
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
 
 
 #pokemon file is read
r = "Pokemon_list.txt"
new_list = []
with open(r, "r", encoding="utf-8") as f:   
    new_list = [(line.strip('\n')) for line in f]

#Start of game
print("Hello player\n")
print("Here are the pokemon you can choose from, press 0-9 for choice: ")

#sequence unpacking
pokemon_list = ["Venasaur(0)", "Blastoise(1)", "Charizard(2)", "Blastoise(3)",
                "Meganium(4)","Typhlosion(5)","Feraligatr(6)","Sceptile(7)",
                                                    "Blaziken(8)","Swampert(9)"]
first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth = pokemon_list

print(f"{first},{second},{third},{fourth},{fifth},{sixth},{seventh},{eighth},{ninth}, {tenth}")

#Create an object for each pokemon 
venasaur = Pokemon("Venasaur",3,"Grass","Poison",80,82,83,80)
charizard = Pokemon("Charizard",6,"Fire","Flying",78,84,78,100)
blastoise = Pokemon("Blastoise",9,"Water","N/A",79,83,100,78)



#Making sure the user inputs a valid option
choice = False
while choice == False:
    p_choice = int(input("Which pokemon do you want?"))
    if p_choice < 0 or p_choice > 9:
        print("this isn't a valid choice!")
    else:
        choice = True
    
#creating a pokemon object based on what pokemon player chose

if p_choice == 0:
    selected = venasaur

elif p_choice == 1:
    selected = charizard

elif p_choice == 2:
    selected = blastoise

print(f"You have chosen {selected.name}!")


    
    
#computer 

c_choice= random.randrange(10)


#creating pokemon object for pokemon that computer chose
if c_choice == 0:
    c_selected = venasaur

elif c_choice == 1:
    c_selected = charizard
    
elif c_choice == 2:
    c_selected = blastoise

print(f"You are facing {c_selected.name}!")



#the battle begins!
#fastest pokemon goes first


if (selected.spe > c_selected.spe):
    #Player's turn
    print(f"{selected.name}'s turn! Movelist: {selected.moves}")
    move_choice = input("What move will you choose?")
    
    if move_choice.casefold() == "Tackle":
        selected.attack(c_selected, "Tackle")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        
        
    elif move_choice.casefold() == "Razor Leaf":
        selected.attack(c_selected, "Razor Leaf")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Water" or c_selected.type2 == "Water":
            print("It was super effective!")
            c_selected.hp -= 20
        elif c_selected.type1 == "Fire" or c_selected.type2 == "Flying":
            print("It wasn't effective...")
            c_selected.hp + 20
    
    elif move_choice.casefold() == "Sludge Bomb":
        selected.attack(c_selected, "Sludge Bomb")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        

    elif move_choice.casefold() == "Petal Dance":
        selected.attack(c_selected, "Petal Dance")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Water" or c_selected.type2 == "Water":
            print("It was super effective!")
            c_selected.hp -= 20
        elif c_selected.type1 == "Fire" or c_selected.type2 == "Flying":
            print("It wasn't effective...")
            c_selected.hp + 20

    elif move_choice.casefold() == "Flamethrower":
        selected.attack(c_selected, "Flamethrower")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Grass" or c_selected.type2 == "Grass":
            print("It was super effective!")
            c_selected.hp -= 20
        elif c_selected.type1 == "Water" or c_selected.type2 == "Water":
            print("It wasn't effective...")
            c_selected.hp + 20
    
    elif move_choice.casefold() == "Air Slash":
        selected.attack(c_selected, "Air Slash")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Grass" or c_selected.type2 == "Grass":
            print("It was super effective!")
            c_selected.hp -= 20
        
    
    elif move_choice.casefold() == "Seismic Toss":
        selected.attack(c_selected, "Seismic Toss")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Grass" or c_selected.type2 == "Poison":
            print("It wasn't effective...")
            c_selected.hp + 20
    
    elif move_choice.casefold() == "Slash":
        selected.attack(c_selected, "Slash")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
    
    elif move_choice.casefold() == "Rapid Spin":
        selected.attack(c_selected, "Rapid Spin")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
    
    elif move_choice.casefold() == "Ice Beam":
        selected.attack(c_selected, "Ice beam")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Grass" or c_selected.type2 == "Flying":
            print("It was super effective!")
            c_selected.hp -= 20
    
    elif move_choice.casefold() == "Hydro Pump":
        selected.attack(c_selected, "Hydro Pump")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Fire" or c_selected.type2 == "Fire":
            print("It was super effective!")
            c_selected.hp -= 20
        elif c_selected.type1 == "Grass" or c_selected.type2 == "Grass":
            print("It wasn't effective...")
            c_selected.hp + 20
    
    elif move_choice.casefold() == "Aqua Tail":
        selected.attack(c_selected, "Aqua Tail")
        print(f"{selected.name} used {move_choice}! {c_selected} now has {c_selected.hp}.")
        if c_selected.type1 == "Fire" or c_selected.type2 == "Fire":
            print("It was super effective!")
            c_selected.hp -= 20
        elif c_selected.type1 == "Grass" or c_selected.type2 == "Grass":
            print("It wasn't effective...")
            c_selected.hp + 20
else:
    
        
match = re.search(regex, str(new_list[p_choice]))

pokemon_attributes = re.search(regex, str(new_list[p_choice]))

#assignments are made
pokemon_p = pokemon_attributes.group(0)

pokemon_name = pokemon_attributes.group(1)

dex_id = pokemon_attributes.group(2)

type1 = pokemon_attributes.group(3)

type2 = pokemon_attributes.group(4)

hp = pokemon_attributes.group(5)

attack = pokemon_attributes.group(6)

defense = pokemon_attributes.group(7)

speed = pokemon_attributes.group(8)

#---------------------

#computer's choosen pokemon

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

#test to see which pokemon was choosen
print(pokemon_p)
print(pokemon_c)
print(pokemon_attributes)





                




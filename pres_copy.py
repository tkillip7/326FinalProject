import re
import random
import pandas as pd
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
first, second, third, fourth, fifth, sixth, seventh, eighth, ninth = pokemon_list

print(f"{first},{second},{third},{fourth},{fifth},{sixth},{seventh},{eighth},{ninth}")




#player chooses pokemon
choice = False

while choice == False:
    p_choice = int(input("Which pokemon do you want?"))
    if p_choice < 0 or p_choice > 9:
        print("this isn't a valid choice!")
    else:
        choice = True
    
#computer 

c_choice= random.randrange(10)


#player chooses pokemon

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





                




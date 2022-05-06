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

    def __init__(self, name, line):
        """initializes a Pokemon and sets it's attributes

        Args:
         health (int): health of pokemon
         type (str): type of pokemon
         speed (int): speed of pokemon


               """

        self.name = name

        if (name == "Venesaur"):

            # select that line that starts with Venesaur
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

            pokemon_attributes = re.search(regex, line)

            self.pokemon_name = pokemon_attributes.group(1)

            self.dex_id = pokemon_attributes.group(2)

            self.type1 = pokemon_attributes.group(3)

            self.type2 = pokemon_attributes.group(4)

            self.hp = pokemon_attributes.group(5)

            self.attack = pokemon_attributes.group(6)

            self.defense = pokemon_attributes.group(7)

            self.speed = pokemon_attributes.group(8)

        elif (name == "Charizard"):

            # select the line that starts with Charizard!
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

            pokemon_attributes = re.search(regex, line)

            self.pokemon_name = pokemon_attributes.group(1)

            self.dex_id = pokemon_attributes.group(2)

            self.type1 = pokemon_attributes.group(3)

            self.type2 = pokemon_attributes.group(4)

            self.hp = pokemon_attributes.group(5)

            self.attack = pokemon_attributes.group(6)

            self.defense = pokemon_attributes.group(7)

            self.speed = pokemon_attributes.group(8)

        elif (name == "Blastoise"):

            # select the line that starts with blastoise!
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

            pokemon_attributes = re.search(regex, line)

            self.pokemon_name = pokemon_attributes.group(1)

            self.dex_id = pokemon_attributes.group(2)

            self.type1 = pokemon_attributes.group(3)

            self.type2 = pokemon_attributes.group(4)

            self.hp = pokemon_attributes.group(5)

            self.attack = pokemon_attributes.group(6)

            self.defense = pokemon_attributes.group(7)

            self.speed = pokemon_attributes.group(8)

        elif (name == "Meganium"):
            # select the line that starts with Meganium!
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

            pokemon_attributes = re.search(regex, line)

            self.pokemon_name = pokemon_attributes.group(1)

            self.dex_id = pokemon_attributes.group(2)

            self.type1 = pokemon_attributes.group(3)

            self.type2 = pokemon_attributes.group(4)

            self.hp = pokemon_attributes.group(5)

            self.attack = pokemon_attributes.group(6)

            self.defense = pokemon_attributes.group(7)

            self.speed = pokemon_attributes.group(8)

        elif (name == "Typhlosion"):
            # select the line that starts with Typhlosion
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

            pokemon_attributes = re.search(regex, line)

            self.pokemon_name = pokemon_attributes.group(1)

            self.dex_id = pokemon_attributes.group(2)

            self.type1 = pokemon_attributes.group(3)

            self.type2 = pokemon_attributes.group(4)

            self.hp = pokemon_attributes.group(5)

            self.attack = pokemon_attributes.group(6)

            self.defense = pokemon_attributes.group(7)

            self.speed = pokemon_attributes.group(8)

        elif (name == "Feraligatr"):

            # Select the line that starts with Feraligatr
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

            pokemon_attributes = re.search(regex, line)

            self.pokemon_name = pokemon_attributes.group(1)

            self.dex_id = pokemon_attributes.group(2)

            self.type1 = pokemon_attributes.group(3)

            self.type2 = pokemon_attributes.group(4)

            self.hp = pokemon_attributes.group(5)

            self.attack = pokemon_attributes.group(6)

            self.defense = pokemon_attributes.group(7)

            self.speed = pokemon_attributes.group(8)

        # initialize list for pokemon moves
        venasaur_moves = []
        charizard_moves = []
        blastoise_moves = []
        meganium_moves = []
        typhlosion_moves = []
        feraligatr_moves = []

        # pandas here for the moves

        # Going to filter df to specific Pokemon ID's so it'll be easier to
        # access their specific move sets
        df = pd.read_csv("Pokemon_Moves (1).csv")

        df_2 = pd.read_csv("Pokemon (4).csv")

        # using pandas to initialize the move list for each pokemon

        # if the pokemon is venasaur
        # filter only on Dex_ID 3 for venasaur
        if self.pokemon_name == "Vensaur":
            filter_3 = df["Dex_ID"] == 3
            v_moves_filter = df[filter_3]

            venasaur_moves = v_moves_filter["Move_Name"].tolist()
            self.moves = venasaur_moves

        # do the same for the rest of the pokemon

        elif self.pokemon_name == "Charizard":
            filter_6 = df["Dex_ID"] == 6
            c_moves_filter = df[filter_6]

            charizard_moves = c_moves_filter["Move_Name"].tolist()
            self.moves = charizard_moves

        elif self.pokemon_name == "Blastoise":
            filter_9 = df["Dex_ID"] == 9
            b_moves_filter = df[filter_9]

            blastoise_moves = b_moves_filter["Move_Name"].tolist()
            self.moves = blastoise_moves

        elif self.pokemon_name == "Meganium":
            filter_154 = df["Dex_ID"] == 154
            m_moves_filter = df[filter_154]

            meganium_moves = m_moves_filter["Move_Name"].tolist()
            self.moves = meganium_moves

        elif self.pokemon_name == "Typhlosion":
            filter_157 = df["Dex_ID"] == 157
            t_moves_filter = df[filter_157]

            typhlosion_moves = t_moves_filter["Move_Name"].tolist()
            self.moves = typhlosion_moves

        elif self.pokemon_name == "Feraligatr":
            filter_160 = df["Dex_ID"] == 160
            f_moves_filter = df[filter_160]

            feraligatr_moves = f_moves_filter["Move_Name"].tolist()
            self.moves = feraligatr_moves


def read_pokemon(path):
    """Opens pokemons.txt file, convert each line to a Pokemon object, then
    returns a list with one instance of Pokemon per line in the file

    Args:
        path (str): path to pokemons.txt file
    """

    with open(path, "r", encoding="utf-8") as f:

        new_list = [Pokemon(line.strip('\n')) for line in f]

        return new_list


def __sub__(self):
    test = "We'll just do this later"


class Player:
    """Abstract class for player
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Take a turn for the player, pokemon with higher speed attacks 
        first"""


class Human(Player):
    """Class representing the human player

    Args:
        Player (class): subclass of Player

    """

    def __init__(self, name):
        super().__init(name)

    def get_name(self):
        """
        Give name to human player
        """
        print("Hello Human!\n")
        name = input("Please enter your name: ")
        print(f"What's up {name}!")


class Computer(Player):
    """Class representing the computer player

    Args:
        Player (class): subclass of Player
    """

    def __init__(self, name):
        super().__init__(name)

    def get_name(self):
        """
            Give name to computer player
        """
        print("Computer needs a name!!\n")
        name = input("Give computer a name: ")
        print(f"What's up {name} ....")



def main(test, other):
    "start game"
    "do something like game.play()"
    ""


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)

  # game.play()

import re 
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
   def __init__(self, line):
       """initializes a Pokemon and sets it's attributes
       
       Args:
        health (int): health of pokemon
        type (str): type of pokemon
        speed (int): speed of pokemon
        
        
              """
       "use pandas here, take the info from each column in the csv file"
       "and then set the attribute to that"
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
    

   def move_set(self,more):
        """depending on what pokemon was chosen, use regex to find the name of 
        the
        chosen pokemon, then take the 4 moves in the same line of that pokemon 
        name"""
        #read in txt file, use regex to set moves into variables>
        
        


def read_pokemon(path):
    """Opens pokemons.txt file, convert each line to a Pokemon object, then
    returns a list with one instance of Pokemon per line in the file

    Args:
        path (str): path to pokemons.txt file
    """      
    with open(path, "r", encoding="utf-8") as f:   
         
        new_list = [Pokemon(line.strip('\n')) for line in f]
        
        return new_list
    
    
class Player:
    """Abstract class for player
    """
    
    def turn(self):
        """Take a turn for the player, pokemon with higher speed attacks 
        first"""


class Human(Player):
    """Class representing the human player
    
    Args:
        Player (class): subclass of Player
    
    """
    
    def turn(self):
        """Player takes a turn, inputs what move they want to attack opponent 
        with
        determine if it hits, then remove damage from opposing pokemon and 
        display health
        "Player 1, go!
                *choose a move*
                
                if move isn't super effective, apply base damage
                if move is weak, apply less damage
                if move is normal, apply base damage
                
                subtract the damage from opponent HP
        """
        test = "hi"
    


class Computer(Player):
    """Class representing the computer player

    Args:
        Player (class): subclass of Player
    """
    
    def turn(self):
        """computer player takes a turn and chooses a random move to attack with
        if it hits, remove damage froom opposiing pokemon and display health
        
        "Player 2, go!
                *choose a move*
                
                if move isn't super effective, apply base damage
                if move is weak, apply less damage
                if move is normal, apply base damage
                
                subtract the damage from opponent HP
        """
        test = "hi"
       
      

    
     
  
class Game:
    """Initializes the battle between the pokemon. Includes move selection and 
    damage            
     calculations
    
    """
    def __init__(self):
       temp = "hi"
  
      
    def turn(self, Player):
        """turn for each player

        Args:
            Player (class): the player who's turn it is
        """
        
                """
                while player1.health > 0 or player2.health > 0:
                if player1 is faster, player1.turn()
                else player2.turn()
                
                "Player 1, go!
                *choose a move*
                
                if move isn't super effective, apply base damage
                if move is weak, apply less damage
                if move is normal, apply base damage
                
                subtract the damage from opponent HP
                """
      
      
    def __sub__(self,move):
        """Checks the damage the selected move would do to the opposing pokemon.
	        Accounts for attack Stat, attack power of the move, defense stat, 
         typing, 
   	    Args:
      	    arglist (list of str): arguments from the command line.
 	    Returns:
       	    namespace: the parsed arguments, as a namespace.
        """
        temp = "hi"
  
      
    def reset():
        temp = "hi"
        
    def play():
        """Play the pokemon game
        """

def main(test,other):
    "start game"
    "do something like game.play()"
    ""

if __name__ == "__main__":
   args = parse_args(sys.argv[1:])
   main(args.file)
 
 #game.play()
 

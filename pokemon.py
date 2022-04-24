 
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
   def __init__(self,health,type,speed,choices):
       """initializes a Pokemon and sets it's attributes
       
       Args:
        health (int): health of pokemon
        type (str): type of pokemon
        speed (int): speed of pokemon
        choices (list): list of what pokemon the player can pick 
        
              """
       "use pandas here, take the info from each column in the csv file"
       "and then set the attribute to that"
       self.health = health
       
       
       self.type = type
       
       self.speed = speed 
       
       self.choices = choices
    

   def move_set(self,more):
        """depending on what pokemon was chosen, use regex to find the name of the
        chosen pokemon, then take the 4 moves in the same line of that pokemon name"""
        #read in csv file, use regex to set moves into variables>
        
        


def read_pokemon(path):
    """Opens pokemons.txt file, convert each line to a Pokemon object, then
    returns a list with one instance of Pokemon per line in the file

    Args:
        path (str): path to pokemons.txt file
    """      
    
    
class Player:
    """Abstract class for player
    """
    
    def turn(self):
        """Take a turn for the player, pokemon with higher speed attacks first"""


class Human(Player):
    """Class representing the human player
    
    Args:
        Player (class): subclass of Player"""
    
    def turn(self):
        """Player takes a turn, inputs what move they want to attack opponent with
        determine if it hits, then remove damage from opposing pokemon an display health
        
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
        """
        test = "hi"
       
      

    
     
  
class Game:
    """Initializes the battle between the pokemon. Includes move selection and damage            
     calculations
    
    """
    def __init__(self):
       temp = "hi"
  
      
    def turn(self, Player):
        """turn for each player

        Args:
            Player (class): the player who's turn it is
        """
      
      
    def damage_calc(self,move):
        """Checks the damage the selected move would do to the opposing pokemon.
	        Accounts for attack Stat, attack power of the move, defense stat, typing, 
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
 

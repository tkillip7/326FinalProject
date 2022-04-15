 
class Pokemon:
   """ Initializes the 6 pokemon and their attributes.
   
   Attributes:
        health (int): health of the pokemon
        damage (int): base damage of the pokemon
        type (str): the type of the pokemon
        speed (int): how fast the pokemon is
   """
   def __init__(self,health,damage,type,speed,choices):
       """initializes a Pokemon and sets it's attributes
       
       Args:
        health (int): health of pokemon
        damage (int): damage pokemon can do
        
              """
       
       self.health = health
       
       self.damage = damage 
       
       self.type = type
       
       self.speed = speed 
       
       self.choices = choices
    

   def move_set(self,more):
        """read in from file, depending on what we read, give it a set of moves"""
        test = "hi"
        
       
       
      
def read_pokemon(path):
    """Opens pokemons.txt file, convert each line to a Pokemon object, then
    returns a list with one instance of Pokemon per line in the file

    Args:
        path (str): path to pokemons.txt file
    """
       
     
  
class Fight:
    """Initializes the battle between the pokemon. Includes move selection and damage            
     calculations
    
    """
    def __init__(self):
       temp = "hi"
  
      
    def move_select(self):
       temp = "hi"
      
      
    def damage_calc(self,move):
        """Checks the damage the selected move would do to the opposing pokemon.
	        Accounts for attack Stat, attack power of the move, defense stat, typing, 
   	    Args:
      	    arglist (list of str): arguments from the command line.
 	    Returns:
       	    namespace: the parsed arguments, as a namespace.
        """
        temp = "hi"
  
    def accuracy(self,move):
        """Performs a check to see if the selected move will connect. Random Number Generator for choosing accuracy. 
        
        """
        temp = "hi"
      
    def reset():
        temp = "hi"

def main(test,yourmom):
    test = "hi"

if __name__ == "__main__":
   args = parse_args(sys.argv[1:])
   main(args.file)
 
 
 
 
 
 
 
 
 
    """Pokemon class:
    
    initialize pokemon
    
    move set
    
    
    
    
    
    Fight class:
    
    player chooses pokemon
    
    computer chooses pokemon 
    
    player chooses move
    
    computer chooses move
    
    repeat until pokemon has fainted
    
    reset, choose option to keep same pokemon or new ones 
    
    """


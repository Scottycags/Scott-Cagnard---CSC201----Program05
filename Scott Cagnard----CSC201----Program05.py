#Scott Cagnard
#Program Assignment 5

class Treasure():         #Create a parent class called treasure
    def __init__(self, name):    #Create an instane function given the name of a treasure
        self.name = name
    def value_is(self):
        return self.value
    def look_at(self):
        return "%s %s and is worth %s" % (self.name, self.description, self.value)
    def pick_up(self):
        return "%s picks up %s" % (self.player_name, self.na

#We create functions in the base class for different purposes
#value_is will return the value of the treasure object in terms of a gold total
#look_at will return all the characteristics of the treasure object
#pick_up will make the player pick up the designated treasure object

class Armor(Treasure):     #Create an Armor class which will be a subclass of the Treasure class
    kind = "This is an armor treasure object"     #Designate the kind of treasure it is
    def __init__(self, name, description, value):
        self.description = description
        self.value = value
        super().__init__(name)     #Acquire all the functions of the parent class
    def wear(self):
            return "player puts on %s" % self.name
    def remove(self):
            return "player removes %s" % self.name

#wear will make the player put on the designated armor
#remove will make the player take off the designated armor

class Weapon(Treasure):               #Create a weapon subclass
    kind = "This is a weapon treasure object"    #Identify the type of treasure
    def __init__(self, name, description, value):
        self.description = description
        self.value = value
        super().__init__(name)        #Acquire all the functions/variables of parent class

    def wield(self):
        return "player wields %s" % self.name

    def unwield(self):
        return "player unwields %s" % self.name

#Wield will make the player wield the designated oweapon
#Unwield will make the player unwield the designated weapon
     
class Food(Treasure):                 #Create a food subclass
    kind = "This is a food treasure object"    #Identify the type of treasure
    def __init__(self, name, description, value, nutr_value):
        self.description = description
        self.value = value
        self.nutr_value = nutr_value
        super().__init__(name)        #Acquire all the functions/variables from parent class
    def eat(self):
        return "player eats %s which has nutrition value of %s" % (self.name, self.nutr_value)

#eat will make the player eat the designated food object and will alsp provide a nutrition value

class Gold(Treasure):     #Create a gold subclass
    kind = "This is a gold treasure object"      #Identify the type of treasure object
    def __init__(self, name, description, value)
        self.description = description
        self.value = value
        super().__init__(name)     #Acquire all characteristics/variables from parent class

class Coin(Gold):   #Create a gold coin treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Coin", description = "is a small round gold object", value = "5 gold total")


class Gun(Weapon):    #Create a gun treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Gun", description = "fires 10 bullets", value = "25 gold total")
    
class Sword(Weapon):      #Create a sword treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Sword", description = "has a sharp blade", value = "20 gold total")

class Rock(Weapon):     #Create a rock treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Rock", description = "is a hard rough object", value = "5 gold total")

class Gold_Armor(Armor):     #Create a gold armor treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Gold Armor",description = "is the highest armor", value = "15 gold total")
        self.defenselvl = 30
            
class Silver_Armor(Armor):    #Create a silver armor treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Silver Armor",description = "is the middle armor", value = "10 gold total")
        self.defenselvl = 20
            
class Bronze_Armor(Armor):     #Create a bronze treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Bronze Armor",description = "is the lowest armor", value = "5 gold total")
        self.defenselvl = 10
        
class Chicken(Food):      #Create a chicken treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Chicken",description = "is small with feathers and a beak",value = "25 gold total", nutr_value = 30)

class Fish(Food):       #Create a fish treasure object with specific characteristics
    def __init__(self):
        super().__init__(name = "Fish",description = "lives in the sea",value = "20 gold total", nutr_value = 25)

class Player():        #Create a player class with certain base attributes
    def __init__(self):
        self.location_x, self.location_y = world.starting_position
        self.explvl = 0
        self.health = 30

    def kill_monster(self):     #A player can kill a moster
        self.explvl += 5     #When a player kills a monster it receives experience level points
        return "player kills monster"    #Return results of action

    def explevel(self):     #Acquire current experience level whenever needed
        return self.explvl

    def attacked(self):     #Create function where player is attacked
        self.health -= 4      #Player's health will decrease
        return "You were attacked by a monster and your health is now %s" % self.health

   
    def move(self, dx, dy):
        self.location_x += dx       #Allow the player to move in any certain direction
        self.location_y += dy
        return "%s, %s is your new location" % (self.location_x, self.location_y)

    def move_north(self):
        self.move(dx = 0, dy = -1)

    def move_south(self):
        self.move(dx = 0, dy = 1)

    def move_east(self):
        self.move(dx = 1, dy = 0)

    def move_west(self):
        self.move(dx = -1, dy = 0)
        
#Allow the player to move north, south, east, or west



    





    

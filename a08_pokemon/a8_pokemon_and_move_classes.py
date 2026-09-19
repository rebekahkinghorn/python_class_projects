# Rebekah Kinghorn
# Pokemon and Move Classes


import random

"""PART ONE"""

#let's create a class!
class Move:
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points) -> None:
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points
    
    #method to return the move info
    def get_info(self):
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points" 
    
    #method to randomly generate the attack value
    def generate_attack_value(self):
        return random.randint(self.low_attack_points,self.high_attack_points)


#making a bunch of Move objects 
tackle = Move("Tackle", "Normal", 5, 20)
quick_attack = Move("Quick Attack", "Normal", 6, 25)
slash = Move("Slash", "Normal", 10, 30)
flamethrower = Move("Flamethrower", "Fire", 5, 30)
ember = Move("Ember", "Fire", 10, 20)
water_gun = Move("Water Gun", "Water", 5, 15)
hydro_pump = Move("Hydro Pump", "Water", 20, 25)
vine_whip = Move("Vine Whip", "Grass", 10, 25)
solar_beam = Move("Solar Beam", "Grass", 18, 27)


#making a list that stores all of my Move objects
move_objects_list = [tackle, quick_attack, slash, flamethrower, ember, water_gun, hydro_pump, vine_whip, solar_beam]



#initialize for the loop
move_count = 1

#making a loop that generates attack values and then deletes move
for move in move_objects_list:
    randomly_selected_move = move_objects_list[random.randint(0,len(move_objects_list)-1)]
    print(Move.get_info(randomly_selected_move))
    print(f"Generated attack value: {Move.generate_attack_value(randomly_selected_move)}")
    move_objects_list.remove(randomly_selected_move)

    move_count += 1
    if move_count > 5:
        break

input("Press enter to continue...")


"""PART TWO"""

class Pokemon:
    def __init__(self, name, elemental_type, hit_points) -> None:
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points
    
    def get_info(self):
        return f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"
    
    def heal(self):
        self.hit_points = self.hit_points + 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")

    
#making a bunch of Pokemon objects
bulbasaur = Pokemon("Bulbasaur", "Grass", 60)
charmander = Pokemon("Charmander", "Fire", 55)
squirtle = Pokemon("Squirtle", "Water", 65)


print(Pokemon.get_info(charmander))
Pokemon.heal(charmander)
print(Pokemon.get_info(charmander))


#making a list with the Pokemon objects
pokemons_list = [bulbasaur, charmander, squirtle]


#initializing the loop
pokemon_count = 1

#making a loop that prints all of their info
for pokemon in pokemons_list:
    print(Pokemon.get_info(pokemon))


"""REBEKAH"""

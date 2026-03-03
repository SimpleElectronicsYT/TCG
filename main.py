import random
import time
from pokemon import Pokemon
from card_data import all_cards

def populate_pokemon():
    # Creates a 'Pokemon' object from all the pokemon in 'card_data.py' and stores it in a dict
    
    card_dict = {}
    for individual_card in all_cards:
        card_object = individual_card["id"]
        card_object = Pokemon(individual_card)
        card_dict[individual_card["id"]] = card_object
    return card_dict
        

def main():
    # Empty list to store the card ID values for randomizer use
    id_key_list = []
    # Empty list to store the two pokemon who will fight
    active_pokemon_list = []
    
    # Start the game by populating the cards into a master dictionary with card_id: card_object pairs
    card_dict = populate_pokemon()
    
    # Print to the terminal which cards have been successfully loaded and made into objects
    for card in card_dict:
        print(f"{card_dict[card].name} ({card}) card has been loaded successfully!")
        # Make a list of the dictionary keys so that the randomizer can pick two to fight each other
        id_key_list.append(card)
    
    # Game loop will have to come later - pick two pokemon at random to fight each other
    active_pokemon_list = random.sample(id_key_list, 2)
    
    player_one = card_dict[active_pokemon_list[0]]
    player_two = card_dict[active_pokemon_list[1]]
    
    print(player_one)
    print(player_two)
    """
    # instantiate the pokemon cards from the 'all cards' module which is a list of card dicts
    # each object should be called by the id of the card - will have to deal with repeat cards later
    # for now, the ID will be the object's name
    for card in all_cards:
        id = card["id"]
        id = Pokemon(card)
    
    # pick one at random to start
    first_turn = random.choice(["charmander", "squirtle"])
    
    # set out objects to generic variables to make further code easier
    if first_turn == "charmander":
        first = charmander
        second = squirtle
    else:
        first = squirtle
        second = charmander
        
    # annouce who won the coin toss
    print(f"{first.name} won the coin toss! It will go first!")
    print("")
    round = 1
    
    
    # ensure that both pokemon are healthy and do the game loop
    while charmander.hp > 0 and squirtle.hp > 0:
        
        print(f"Round {round}!")
        print("")
        
        # ensure that the first attacker has enough hp to attack
        if first.hp > 0:
            first.attack(second)
            print(f"{second.name} has {second.hp} hp remaining!")
        
        if first.hp <= 0:
            print(f"{first.name} has fainted!")
            break
            
        if second.hp <= 0:
            print(f"{second.name} has fainted!")
            break
        
        print(" ")
        # pause a bit to let the 'player' read
        time.sleep(5)
        
        # ensure that the second attacker has enough hp to attack
        if second.hp > 0:
            second.attack(first)
            print(f"{first.name} has {first.hp} hp remaining!")
            
        # check for any fainters
        if first.hp <= 0:
            print(f"{first.name} has fainted!")
            break
            
        if second.hp <= 0:
            print(f"{second.name} has fainted!")
            break
        
        print("-------------------------")
        # pause a bit to let the 'player' read
        time.sleep(5)
        
        round += 1
        """
    
    quit()

if __name__ == "__main__":
    main()
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
    
    print("------------------")
    # Tracking the rounds
    round = 0
    
    while player_one.is_alive() and player_two.is_alive():
        round += 1
        print(f"Round {round}!")
        print("------------------")
        time.sleep(5)
        attack = random.randint(0, len(player_one.attacks) -1)
        player_one.attack(player_two, attack)
        time.sleep(10)
        attack = random.randint(0, len(player_two.attacks) -1)
        player_two.attack(player_one, attack)
        time.sleep(5)
        
    quit()

if __name__ == "__main__":
    main()
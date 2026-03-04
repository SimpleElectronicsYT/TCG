import random
import time
import copy
from pokemon import Pokemon
from card_data import all_cards

def populate_pokemon():
    # Creates a 'Pokemon' object from all the pokemon in 'card_data.py' and stores it in a dict
    
    card_dict = {}
    for individual_card in all_cards:
        card_object = Pokemon(individual_card)
        card_dict[individual_card["id"]] = card_object
    return card_dict

def user_choice(card_dict, id_key_list):
    # Lists all potential pokemon to the user and asks the user to pick one
    print("please choose a Pokémon to fight for you")
    number = 1
    for card in card_dict.values():
        print(f"{number}. {card}")
        number += 1
    print("")
    user_input = int(input("Select your pokémon by typing the number associated with your pokémon choice: "))
    return card_dict[id_key_list[user_input - 1]]

def cpu_choice(card_dict, id_key_list):
    random_choice = random.choice(id_key_list)
    return card_dict[random_choice]

def main():
    # Empty list to store the card ID values for randomizer use
    id_key_list = []
    
    # Start the game by populating the cards into a master dictionary with card_id: card_object pairs
    card_dict = populate_pokemon()
    
    # Print to the terminal which cards have been successfully loaded and made into objects
    for card in card_dict:
        print(f"{card_dict[card].name} ({card}) card has been loaded successfully!")
        # Make a list of the dictionary keys so that the randomizer can pick two to fight each other
        id_key_list.append(card)
    
    user = copy.deepcopy(user_choice(card_dict, id_key_list))
    cpu = copy.deepcopy(cpu_choice(card_dict, id_key_list))
    print("")
    print(f"You have selected {user}, get ready for battle!")
    print(f"Your Opponent has selected {cpu}!")
    print("")
    user.list_attacks()
    
    # Tracking the rounds
    round = 0
    
    
    """while player_one.is_alive() and player_two.is_alive():
        round += 1
        print(f"Round {round}!")
        print("------------------")
        time.sleep(5)
        attack = random.randint(0, len(player_one.attacks) -1)
        player_one.attack(player_two, attack)
        if not player_two.is_alive():
            print(f"{player_two.name} has fainted!")
            print(f"Good game!")
            break
            
        time.sleep(5)
        attack = random.randint(0, len(player_two.attacks) -1)
        player_two.attack(player_one, attack)
        if not player_one.is_alive():
            print(f"{player_one.name} has fainted!")
            print(f"Good game!")
            break
        time.sleep(5)"""
        
    quit()

if __name__ == "__main__":
    main()
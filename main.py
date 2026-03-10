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

def print_round(round):
    print(f"Round {round}!")
    print("------------------")
    print("")
    time.sleep(2)
    
def print_turn():
    print("It's your turn!")
    print("")
    time.sleep(1)

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
        
    # Tracking the rounds
    round = 0
    
    while user.is_alive() and cpu.is_alive():
        
        #Round handling
        round += 1
        print_round(round)
        print_turn()
        
        #User turn handling
        user.list_attacks()
        user_attack = int(input("Select your attack by typing the number associated with your attack choice: "))
        print("")
        user.attack(cpu, user_attack - 1)
        
        
        #CPU turn handling
        cpu.list_attacks()
        cpu_attack = random.randint(1, len(cpu.attacks))
        time.sleep(5)
        print(f"Your Opponent chooses: {cpu.attacks[cpu_attack -1]["name"]}!")
        time.sleep(2)
        cpu.attack(user, cpu_attack -1)
    
    quit()

if __name__ == "__main__":
    main()
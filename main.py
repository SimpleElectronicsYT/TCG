import random
import time
from pokemon import Pokemon
from card_data import all_cards

def main():
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
        
    
    quit()

if __name__ == "__main__":
    main()
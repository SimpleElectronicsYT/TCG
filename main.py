import random
from pokemon import Pokemon

def main():
    # instantiate two pokemon, one a charmander, the other a squirtle
    charmander = Pokemon("Charmander", 50, "fire", "water")
    squirtle = Pokemon("Squirtle", 40, "water", "lightning")
    
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
    
    # ensure that both pokemon are healthy and do the game loop
    while charmander.hp > 0 and squirtle.hp > 0:
        
        # ensure that the first attacker has enough hp to attack
        if first.hp > 0:
            first.attack(second)
            print(f"{first.name} attacks {second.name}!")
            print(f"{second.name} has {second.hp} hp remaining!")
        
        # ensure that the second attacker has enough hp to attack
        if second.hp > 0:
            second.attack(first)
            print(f"{second.name} attacks {first.name}!")
            print(f"{first.name} has {first.hp} hp remaining!")
            
        # check for any fainters
        if first.hp <= 0:
            print(f"{first.name} has fainted!")
            break
            
        if second.hp <= 0:
            print(f"{second.name} has fainted!")
            break
    
    quit()

if __name__ == "__main__":
    main()
import random

class Pokemon:
    def __init__(self, card_data):
        self.id = card_data["id"]
        self.name = card_data["name"]
        self.hp = card_data["hp"]
        self.type = card_data["type"]
        self.stage = card_data["stage"]
        self.weakness = card_data["weakness"]
        self.resistance = card_data["resistance"]
        self.retreat = card_data["retreat"]
        self.evolves_from = card_data["evolves_from"]
        self.pkmn_power = card_data["pkmn_power"]
        self.attacks = card_data["attacks"]        
        self.sleep = False
        self.paralyzed = False
        self.poisoned = False
        self.protected = False
    
    def attack(self, target):
        target.take_damage(self, 10)
        
    def take_damage(self, attacker, damage):
        
        print(f"{attacker.name} uses 'Attack' on {self.name}!")
        
        total_damage = 0
        
        # check for weakness
        if attacker.type == self.weakness:
            total_damage = round(damage * 2, -1)
            print(f"{attacker.name}'s attack is super effective!")
            
        # check for resistance    
        elif attacker.type == self.resistance:
            total_damage = max(0, damage - 30)
            print(f"{attacker.name}'s attack is resisted by {self.name}!")
        
        # just do regular damage if not    
        else:
            total_damage = damage
            
        self.hp -= total_damage
        print(f"{attacker.name} hits {self.name} for {total_damage}!")    
        
        if self.hp < 0:
            self.hp = 0
            
    def flip_coin(self):
        return random.choice(["heads", "tails"])
"""    
class Charmander(Pokemon):
    def __init__(self, name, hp, type, weakness, resistance):
        super().__init__(name, hp, type, weakness, resistance)
        self.moves = [self.scratch(), self.ember()]
        
    def scratch(self, target):
        target.take_damage(self, 10)
        
    def ember(self, target):
        target.take_damage(self, 30)
        
class Squirtle(Pokemon):
    def __init__(self, name, hp, type, weakness, resistance):
        super().__init__(name, hp, type, weakness, resistance)
        self.moves = [self.bubble(), self.withdraw()]
        
    def take_damage(self, attacker, damage):
        super().take_damage(attacker, damage)
        
        print(f"{attacker.name} uses 'Attack' on {self.name}!")
        
        if self.take_no_damage == True:
            print(f"{self.name} protected itself!")
            self.take_no_damage = False
            
        else:
            total_damage = 0
        
            # check for weakness
            if attacker.type == self.weakness:
                total_damage = round(damage * 2, -1)
                print(f"{attacker.name}'s attack is super effective!")
            
            # check for resistance    
            elif attacker.type == self.resistance:
                total_damage = max(0, damage - 30)
                print(f"{attacker.name}'s attack is resisted by {self.name}!")
        
            # just do regular damage if not    
            else:
                total_damage = damage
            
        self.hp -= total_damage
        print(f"{attacker.name} hits {self.name} for {total_damage}!")    
        
        if self.hp < 0:
            self.hp = 0
        
    def bubble(self, target):
        target.take_damage(self, 10)
        
    def withdraw(self):
        result = self.flip_coin()
        print(f"Squirtle used Withdraw! Protects itself from damage on a Heads!")
        print(f"flipping coin....{result}!")
        if result == "heads":
            self.take_no_damage = True
            print(f"{self.name} won't take damage next turn!")
        else:
            self.take_no_damage = False
            print(f"Withdraw has no effect!")
        
        """
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
        # Attacks are a list of dicts
        # "name", "damage", "energy"
        self.attacks = card_data["attacks"]        
        self.sleep = False
        self.paralyzed = False
        self.poisoned = False
        self.protected = False
    
    def __str__(self):
        return f"{self.name}, {self.hp}hp remaining"
        
    def attack(self, target, index):
        # FUTURE - check if enough energy is attached
        damage = 0
        print(f"{self.name} uses {self.attacks[index]['name']}!")
        damage = self.attacks[index]["damage"]
        if self.type == target.weakness:
            damage *= 2
            print("It's super effective!")
        print(f"total damage: {damage}")
        
        target.take_damage(self, damage)
            
        # FUTURE - check for status effects
        # FUTURE - check for secondary effects
        
    def take_damage(self, attacker, damage):
        if self.resistance == attacker.type:
            damage = max(0, damage - 30)
            print(f"{self.name} resists {attacker.name}'s attack!")
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} takes {damage} damage!")
        print(f"{self.name} has {self.hp}hp remaining!")
        print("")
        
        
    def flip_coin(self):
        return random.choice(["heads", "tails"])
    
    def is_alive(self):
        if self.hp <= 0:
            return False
        return True

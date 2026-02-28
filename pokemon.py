class Pokemon:
    def __init__(self, name, hp, type, weakness, resistance):
        self.name = name
        self.hp = hp
        self.type = type
        self.weakness = weakness
        self.resistance = resistance
    
    def attack(self, target):
        target.take_damage(self, 10)
        
    def take_damage(self, attacker, damage):
        total_damage = 0
        
        # check for weakness
        if attacker.type == self.weakness:
            total_damage = round(damage * 2, -1)
            self.hp -= total_damage
            print(f"{attacker.name}'s attack is super effective!")
            print(f"{attacker.name} hits {self.name} for {total_damage}!")
        
        # check for resistance    
        elif attacker.type == self.resistance:
            total_damage = max(0, damage - 30)
            self.hp -= total_damage
            print(f"{attacker.name}'s attack is resisted by {self.name}!")
            print(f"{attacker.name} hits {self.name} for {total_damage}!")
        
        # just do regular damage if not    
        else:
            total_damage = damage
            self.hp -= total_damage
            print(f"{attacker.name} hits {self.name} for {total_damage}!")
            
        if self.hp < 0:
            self.hp = 0
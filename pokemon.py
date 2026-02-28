class Pokemon:
    def __init__(self, name, hp, type, weakness):
        self.name = name
        self.hp = hp
        self.type = type
        self.weakness = weakness
    
    def attack(self, target):
        target.take_damage(self, 10)
        
    def take_damage(self, attacker, damage):
        if attacker.type == self.weakness:
            self.hp -= round(damage * 2, -1)
        else:
            self.hp -= damage
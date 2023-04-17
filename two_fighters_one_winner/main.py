class Fighter():
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        while fighter1.health >= 0 or fighter2.health >= 0:
            fighter1.health -= fighter2.damage_per_attack
            fighter2.health -= fighter1.damage_per_attack
        if fighter1.health <= 0:
            return fighter2.name
        elif fighter2.health <= 0:
            return fighter1.name
    elif first_attacker == fighter2.name:
        while fighter1.health >= 0 or fighter2.health >= 0:
            fighter2.health -= fighter1.damage_per_attack
            fighter1.health -= fighter2.damage_per_attack
            
        if fighter1.health <= 0:
            return fighter2.name
        elif fighter2.health <= 0:
            return fighter1.name

# (Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")
        
# (Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")

# (Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")

# (Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")

# (Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")

# (Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")


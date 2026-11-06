class Skill:
    def __init__(self, name, description, damage=0, healing=0, cooldown=0):
        self.name = name
        self.description = description
        self.damage = damage
        self.healing = healing
        self.cooldown = cooldown

    def use(self, player, monster):
        if self.healing:
            amount = min(self.healing, player.max_hp - player.hp)
            player.hp += amount
            print(f"{self.name} restores {amount} HP.")
        if self.damage and monster:
            monster.hp -= self.damage + player.level
            print(f"{self.name} hits for {self.damage + player.level} damage.")
        player.cooldowns[self.name] = self.cooldown

class Strike(Skill):
    def __init__(self):
        super().__init__("Strike", "A reliable basic attack.", damage=5, cooldown=0)

class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", "A burst of flame.", damage=13, cooldown=2)

class Heal(Skill):
    def __init__(self):
        super().__init__("Heal", "Restore your health.", healing=14, cooldown=3)

class Skills:
    ALL = {"Strike": Strike, "Fireball": Fireball, "Heal": Heal}
    @classmethod
    def make(cls, name):
        return cls.ALL[name]()

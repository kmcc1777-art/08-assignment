import random

class Monster:
    def __init__(self, name, hp, damage, xp, gold, drops):
        self.name, self.hp, self.max_hp = name, hp, hp
        self.damage, self.xp, self.gold, self.drops = damage, xp, gold, drops

    def attack(self, player):
        player.hp = max(0, player.hp - self.damage)
        print(f"{self.name} hits you for {self.damage} damage!")

    def reward(self, player):
        player.gold += self.gold
        player.gain_xp(self.xp)
        print(f"You earned {self.gold} gold.")
        if self.drops and random.random() < 0.65:
            item = random.choice(self.drops)
            player.inventory.append(item)
            print(f"The monster dropped: {item}!")

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 16, 4, 12, 7, ["Potion", "Bomb", "Herb"])

class Wolf(Monster):
    def __init__(self):
        super().__init__("Dire Wolf", 22, 6, 17, 10, ["Wolf Pelt", "Potion"])

class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 28, 7, 22, 13, ["Bomb", "Potion"])

class Ogre(Monster):
    def __init__(self):
        super().__init__("Ogre", 42, 9, 35, 20, ["Super Potion", "Bomb"])

class Dragon(Monster):
    def __init__(self):
        super().__init__("Ashen Dragon", 75, 12, 100, 100, ["Super Potion"])

MONSTERS = {"goblin": Goblin, "wolf": Wolf, "skeleton": Skeleton, "ogre": Ogre, "dragon": Dragon}

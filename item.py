class Item:
    def __init__(self, name, description, price, kind, power):
        self.name, self.description = name, description
        self.price, self.kind, self.power = price, kind, power

ITEMS = {
    "Potion": Item("Potion", "Restores 15 HP.", 10, "heal", 15),
    "Super Potion": Item("Super Potion", "Restores 35 HP.", 25, "heal", 35),
    "Bomb": Item("Bomb", "Deals 18 damage to a monster.", 18, "damage", 18),
    "Herb": Item("Herb", "A fragrant quest herb.", 0, "quest", 0),
    "Wolf Pelt": Item("Wolf Pelt", "Proof of a wolf hunt.", 0, "quest", 0),
}

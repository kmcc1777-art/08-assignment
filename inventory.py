from colorama import Fore
from item import ITEMS

class Inventory:
    def __init__(self, names=None):
        self.items = list(names or [])

    def add(self, name):
        self.items.append(name)

    def remove(self, name):
        if name in self.items:
            self.items.remove(name)
            return True
        return False

    def show(self):
        print(Fore.CYAN + "\n--- Inventory ---")
        if not self.items:
            print("Your bag is empty.")
        else:
            counts = {}
            for name in self.items:
                counts[name] = counts.get(name, 0) + 1
            for name, count in counts.items():
                print(f"{name} x{count} — {ITEMS[name].description}")

    def use(self, player, target=None):
        self.show()
        name = input("Item to use (or Enter to cancel): ").strip()
        if not name:
            return
        if name not in self.items:
            print(Fore.RED + "You don't have that item.")
            return
        item = ITEMS[name]
        if item.kind == "heal":
            if player.hp >= player.max_hp:
                print("Your HP is already full.")
                return
            self.remove(name)
            player.hp = min(player.max_hp, player.hp + item.power)
            print(Fore.GREEN + f"Recovered {item.power} HP.")
        elif item.kind == "damage" and target:
            self.remove(name)
            target.hp -= item.power
            print(Fore.YELLOW + f"The bomb deals {item.power} damage!")
        else:
            print("That item cannot be used here.")

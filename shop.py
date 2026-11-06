from colorama import Fore
from item import ITEMS

class Shop:
    STOCK = ["Potion", "Super Potion", "Bomb"]
    def visit(self, player):
        while True:
            print(Fore.CYAN + f"\n--- Village Shop | Gold: {player.gold} ---")
            for i, name in enumerate(self.STOCK, 1):
                item = ITEMS[name]
                print(f"{i}. {name} — {item.price} gold ({item.description})")
            print("0. Leave")
            choice = input("Buy which item? ").strip()
            if choice == "0": return
            if not choice.isdigit() or not 1 <= int(choice) <= len(self.STOCK):
                print("Invalid selection."); continue
            name = self.STOCK[int(choice)-1]
            price = ITEMS[name].price
            if player.gold < price:
                print(Fore.RED + "Not enough gold.")
            else:
                player.gold -= price
                player.inventory.append(name)
                print(Fore.GREEN + f"Bought {name}.")

import random
from colorama import Fore
from database import get_user, save_user
from player import Player
from inventory import Inventory
from shop import Shop
from game_map import GameMap, MAPS
from monster import MONSTERS
from combat import battle
from npc import NPCS
from quest import QuestManager

class Game:
    def __init__(self, username):
        self.username = username
        self.player = Player(get_user(username))

    def save(self):
        save_user(self.username, self.player.to_dict())

    def move(self):
        direction = input("Move (W/A/S/D), or Enter to cancel: ").strip().lower()
        delta = {"w": (-1,0), "s": (1,0), "a": (0,-1), "d": (0,1)}
        if direction not in delta: return
        r, c = self.player.position
        dr, dc = delta[direction]
        nr, nc = r+dr, c+dc
        layout = MAPS[self.player.map_name]
        if nr < 0 or nr >= len(layout) or nc < 0 or nc >= len(layout[nr]) or layout[nr][nc] == "#":
            print("A wall blocks your way."); return
        self.player.position = [nr, nc]
        self.handle_tile(layout[nr][nc])

    def handle_tile(self, tile):
        p = self.player
        if tile == "N":
            print("Nearby people: Rowan, Mira, Bram, Tessa, Finn")
            name = input("Who do you want to talk to? ").strip()
            if name in NPCS: NPCS[name].talk(p)
            else: print("That person isn't here.")
        elif tile == "S" and p.map_name == "village":
            Shop().visit(p)
        elif tile == "W":
            self.encounter("wolf")
        elif tile == "D":
            if p.quest["main"] < 3:
                print("A sealed force blocks the crater. Advance the main quest first.")
            else:
                if battle(p, MONSTERS["dragon"]()):
                    p.quest["main"] = 4
                    p.won = True
        elif p.map_name == "forest" and random.random() < 0.22:
            self.encounter(random.choice(["goblin", "wolf"]))
        elif p.map_name == "ruins" and random.random() < 0.25:
            self.encounter(random.choice(["skeleton", "ogre"]))

    def encounter(self, kind):
        won = battle(self.player, MONSTERS[kind]())
        if won and kind == "goblin":
            self.player.quest["goblin_done"] = True
        if won and kind == "skeleton":
            self.player.quest["ruins_done"] = True

    def travel(self):
        options = {"village": ["forest"], "forest": ["village", "ruins"], "ruins": ["forest", "crater"], "crater": ["ruins"]}
        print("Travel destinations: " + ", ".join(options[self.player.map_name]))
        dest = input("Travel to: ").strip().lower()
        if dest in options[self.player.map_name]:
            self.player.map_name = dest
            self.player.position = [1, 1]
            print(f"You travel to {dest.title()}.")
        else: print("You cannot travel there from here.")

    def learn_skill(self):
        choices = {"Fireball": (2, 35), "Heal": (3, 50)}
        for name, (level, cost) in choices.items():
            status = "LEARNED" if name in self.player.skills else f"Level {level}, {cost} gold"
            print(f"{name}: {status}")
        name = input("Skill to learn (or Enter to cancel): ").strip()
        if name in choices and name not in self.player.skills:
            level, cost = choices[name]
            if self.player.level >= level and self.player.gold >= cost:
                self.player.gold -= cost
                self.player.skills.append(name)
                print(Fore.GREEN + f"You learned {name}!")
            else: print("You need the required level and gold.")
        elif name: print("That skill is unavailable or already learned.")

    def run(self):
        print(Fore.YELLOW + "\nThe kingdom of Aster is fading. The Shattered Crown has broken,")
        print("and an Ashen Dragon guards its final fragment. Restore the crown!")
        while True:
            p = self.player
            if p.won:
                print(Fore.GREEN + "\n*** VICTORY! You defeated the Final Boss and saved Aster! ***")
            print(Fore.CYAN + f"\n{p.map_name.title()} | HP {p.hp}/{p.max_hp} | Gold {p.gold}")
            print("1. View map  2. Move  3. Travel  4. Talk to NPC")
            print("5. Inventory  6. Character  7. Quests  8. Learn skill")
            print("9. Shop  10. Save and logout  11. Quit")
            choice = input("> ").strip()
            if choice == "1": GameMap(p.map_name).draw(p.position)
            elif choice == "2": self.move()
            elif choice == "3": self.travel()
            elif choice == "4":
                print("NPCs: Rowan, Mira, Bram, Tessa, Finn")
                name = input("Name: ").strip()
                if name in NPCS: NPCS[name].talk(p)
                else: print("No NPC by that name.")
            elif choice == "5": Inventory(p.inventory).use(p)
            elif choice == "6": p.show_stats()
            elif choice == "7": QuestManager(p).show()
            elif choice == "8": self.learn_skill()
            elif choice == "9":
                if p.map_name == "village": Shop().visit(p)
                else: print("The shop is only in the village.")
            elif choice == "10":
                self.save(); print(Fore.GREEN + "Progress saved. Logging out."); break
            elif choice == "11":
                self.save(); print("Progress saved. Goodbye."); break
            else: print("Enter a number from 1 to 11.")
            self.save()

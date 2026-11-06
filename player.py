from colorama import Fore
from skill import Skills

class Player:
    def __init__(self, data):
        self.username = data["username"]
        self.level, self.xp, self.gold = data["level"], data["xp"], data["gold"]
        self.hp, self.max_hp = data["hp"], data["max_hp"]
        self.inventory = data["inventory"]
        self.skills = data["skills"]
        self.map_name, self.position = data["map"], list(data["position"])
        self.quest = data["quest"]
        self.won = data.get("won", False)
        self.cooldowns = {}

    def gain_xp(self, amount):
        self.xp += amount
        print(Fore.GREEN + f"+{amount} XP")
        while self.xp >= self.level * 30 and self.level < 20:
            self.xp -= self.level * 30
            self.level += 1
            self.max_hp += 6
            self.hp = self.max_hp
            print(Fore.YELLOW + f"LEVEL UP! You are now level {self.level}. Max HP increased.")

    def show_stats(self):
        print(Fore.CYAN + f"\n=== {self.username} ===")
        print(f"Level: {self.level} | XP: {self.xp}/{self.level * 30}")
        print(f"HP: {self.hp}/{self.max_hp} | Gold: {self.gold}")
        print("Skills: " + ", ".join(self.skills))
        print(f"Location: {self.map_name} at {self.position}")

    def to_dict(self):
        return {
            "username": self.username, "level": self.level, "xp": self.xp,
            "gold": self.gold, "hp": self.hp, "max_hp": self.max_hp,
            "inventory": self.inventory, "skills": self.skills,
            "map": self.map_name, "position": self.position,
            "quest": self.quest, "won": self.won
        }

from colorama import Fore

MAIN_STEPS = [
    "Speak to Elder Rowan in the village.",
    "Defeat a Goblin in the Forest and return to Rowan.",
    "Find the Sunken Ruins and defeat a Skeleton.",
    "Enter the Dragon's Crater and defeat the Ashen Dragon."
]

class QuestManager:
    def __init__(self, player):
        self.player = player

    def show(self):
        step = self.player.quest["main"]
        print(Fore.CYAN + "\n--- Main Quest: The Shattered Crown ---")
        print(MAIN_STEPS[min(step, 3)])
        print("Side quests:")
        print("Herbal Remedy:", "Complete" if self.player.quest["herbs"] else "Collect an Herb and return to Mira.")
        print("Wolf Trouble:", "Complete" if self.player.quest["wolf"] else "Defeat a Dire Wolf and return to Hunter Bram.")

    def advance_main(self):
        if self.player.quest["main"] < 4:
            self.player.quest["main"] += 1
            if self.player.quest["main"] == 4:
                print(Fore.YELLOW + "The Ashen Dragon has fallen. The Shattered Crown is restored!")
                self.player.won = True

    def complete_side(self, key, reward_gold, reward_xp):
        if not self.player.quest[key]:
            self.player.quest[key] = True
            self.player.gold += reward_gold
            self.player.gain_xp(reward_xp)
            print(Fore.GREEN + f"Quest complete! +{reward_gold} gold and +{reward_xp} XP.")

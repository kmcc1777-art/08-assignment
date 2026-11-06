from colorama import Fore
from quest import QuestManager

class NPC:
    def __init__(self, name, dialogue):
        self.name, self.dialogue = name, dialogue
    def talk(self, player):
        print(Fore.MAGENTA + f"\n{self.name}: \"{self.dialogue}\"")

class ElderRowan(NPC):
    def __init__(self):
        super().__init__("Elder Rowan", "The crown's fragments are guarded by monsters. Follow the old road, and end the dragon's reign.")
    def talk(self, player):
        super().talk(player)
        q = QuestManager(player)
        step = player.quest["main"]
        if step == 0:
            print("Rowan: Your journey begins. Find a goblin in the Forest.")
            q.advance_main()
        elif step == 1 and player.quest.get("goblin_done"):
            print("Rowan: The forest is safer. Seek the Sunken Ruins.")
            q.advance_main()
        elif step == 2 and player.quest.get("ruins_done"):
            print("Rowan: The crater lies beyond the ruins. Face the dragon.")
            q.advance_main()
        elif step == 3 and player.won:
            print("Rowan: You are the hero our kingdom needed.")
        else:
            print("Rowan: Keep moving. Your quest is not finished.")

class Mira(NPC):
    def __init__(self): super().__init__("Mira the Herbalist", "Bring me one Herb and I'll reward your kindness.")
    def talk(self, player):
        super().talk(player)
        if "Herb" in player.inventory and not player.quest["herbs"]:
            player.inventory.remove("Herb")
            QuestManager(player).complete_side("herbs", 20, 15)

class Bram(NPC):
    def __init__(self): super().__init__("Hunter Bram", "A Dire Wolf stalks the forest. Bring proof of the hunt.")
    def talk(self, player):
        super().talk(player)
        if "Wolf Pelt" in player.inventory and not player.quest["wolf"]:
            player.inventory.remove("Wolf Pelt")
            QuestManager(player).complete_side("wolf", 25, 20)

class Tessa(NPC):
    def __init__(self): super().__init__("Tessa the Smith", "A good blade is worth more than a brave boast. Bombs are useful too.")
    def talk(self, player): super().talk(player)

class Finn(NPC):
    def __init__(self): super().__init__("Finn the Wanderer", "The ruins are full of skeletons. Watch your health, traveler.")
    def talk(self, player): super().talk(player)

NPCS = {"Rowan": ElderRowan(), "Mira": Mira(), "Bram": Bram(), "Tessa": Tessa(), "Finn": Finn()}

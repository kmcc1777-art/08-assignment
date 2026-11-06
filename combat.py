from colorama import Fore
from skill import Skills

def battle(player, monster):
    print(Fore.RED + f"\nA {monster.name} appears! ({monster.hp} HP)")
    while monster.hp > 0 and player.hp > 0:
        print(f"\nYour HP: {player.hp}/{player.max_hp} | {monster.name}: {max(0, monster.hp)} HP")
        print("1. Attack  2. Skill  3. Use item  4. Run")
        choice = input("> ").strip()
        if choice == "1":
            damage = 6 + player.level
            monster.hp -= damage
            print(Fore.YELLOW + f"You deal {damage} damage.")
        elif choice == "2":
            print("Skills: " + ", ".join(player.skills))
            name = input("Skill name: ").strip()
            if name not in player.skills:
                print("You have not learned that skill.")
                continue
            skill = Skills.make(name)
            if player.cooldowns.get(name, 0) > 0:
                print(f"{name} is on cooldown for {player.cooldowns[name]} more turn(s).")
                continue
            skill.use(player, monster)
        elif choice == "3":
            from inventory import Inventory
            Inventory(player.inventory).use(player, monster)
        elif choice == "4":
            print("You escaped!")
            return False
        else:
            print("Choose 1, 2, 3, or 4.")
            continue

        if monster.hp <= 0:
            break
        monster.attack(player)
        for key in list(player.cooldowns):
            player.cooldowns[key] = max(0, player.cooldowns[key] - 1)

    if player.hp <= 0:
        print(Fore.RED + "You have been defeated. You wake up at the village with half HP.")
        player.hp = max(1, player.max_hp // 2)
        player.map_name, player.position = "village", [1, 1]
        return False
    print(Fore.GREEN + f"You defeated the {monster.name}!")
    monster.reward(player)
    return True

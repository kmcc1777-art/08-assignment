# The Shattered Crown — Terminal RPG

## Requirements
- Python 3.10+
- `uv` installed

## Setup
Open a terminal in this folder and run:

```bash
uv init
uv add colorama tinydb
uv run python main.py
```

If your class specifically requires the command `uv add colorama`, run that too (TinyDB is also required by this project).

You can alternatively use:
```bash
python -m pip install colorama tinydb
python main.py
```

## How to play
1. Register an account, then log in.
2. Use the numbered menu. On the map, `W/A/S/D` moves up/left/down/right.
3. Visit NPCs, complete the main quest and side quests, buy supplies, and learn skills.
4. Travel between Village, Forest, Ruins, and Crater.
5. Save and log out. Your account and progress are stored in `rpg_data.json`.

## Map legend
`@` player, `#` wall, `N` NPC, `S` shop, `W` wolf encounter, `D` final boss.

## Files
- `main.py`: program entry point and account menu
- `auth.py`, `database.py`: registration, login, TinyDB persistence
- `game.py`: main game loop, movement, travel, menus
- `player.py`: player stats, leveling, save format
- `monster.py`, `combat.py`: monster subclasses and battle loop
- `skill.py`: skill base class and skill subclasses
- `item.py`, `inventory.py`: item definitions and item use
- `quest.py`, `npc.py`: main quest, side quests, NPC dialogue
- `shop.py`: purchases
- `game_map.py`: map layouts and map display
- `config.py`: shared game constants

## Important quest route
- Talk to Rowan in the Village to begin.
- Travel to the Forest and defeat a Goblin. Return and speak to Rowan.
- Travel to the Ruins and defeat a Skeleton. Return and speak to Rowan.
- Travel to the Crater and defeat the Ashen Dragon.
- Side quests: bring an Herb to Mira; bring a Wolf Pelt to Bram.

## Study guide: core programming ideas
- **Inheritance:** `Goblin`, `Wolf`, `Skeleton`, `Ogre`, and `Dragon` inherit from `Monster`. `Strike`, `Fireball`, and `Heal` inherit from `Skill`.
- **Encapsulation:** player data and behavior live in the `Player` class; inventory behavior lives in `Inventory`.
- **Persistence:** `database.py` uses TinyDB to store one record per account in `rpg_data.json`.
- **Game loop:** `Game.run()` repeatedly displays a menu, gets input, calls the matching method, and saves.
- **Validation:** menu choices, movement directions, item names, account names, passwords, shop choices, and skill learning are checked before use.

Read each `.py` file and make sure you can explain the classes, imports, conditionals, loops, and save/load flow before your midterm.

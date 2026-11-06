from colorama import Fore

MAPS = {
    "village": [
        "###########",
        "#P..N...S.#",
        "#..##.....#",
        "#.........#",
        "#..N...N..#",
        "###########"
    ],
    "forest": [
        "#############",
        "#P..#....W..#",
        "#...#..##...#",
        "#......#....#",
        "##.##..#..N.#",
        "#...........#",
        "#############"
    ],
    "ruins": [
        "##############",
        "#P....#......#",
        "#.##..#..##..#",
        "#......S.....#",
        "#..####...#..#",
        "#......N.....#",
        "##############"
    ],
    "crater": [
        "#############",
        "#P....#.....#",
        "#.##..#..##.#",
        "#...........#",
        "#..####.....#",
        "#......D....#",
        "#############"
    ]
}

class GameMap:
    def __init__(self, name): self.name = name
    def draw(self, position):
        layout = MAPS[self.name]
        print(Fore.CYAN + f"\n--- {self.name.title()} ---")
        for r, line in enumerate(layout):
            out = ""
            for c, char in enumerate(line):
                if [r, c] == position: out += Fore.GREEN + "@"
                elif char == "#": out += Fore.WHITE + "#"
                elif char in "NWDS": out += Fore.YELLOW + char
                else: out += Fore.WHITE + "."
            print(out)
        print("Legend: @ you | # wall | N NPC | S shop | W wolf area | D dragon")

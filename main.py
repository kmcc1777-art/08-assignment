from colorama import init, Fore, Style
from auth import register, login
from game import Game

def main():
    init(autoreset=True)
    print(Fore.CYAN + Style.BRIGHT + "\n=== THE SHATTERED CROWN ===")
    print(Fore.YELLOW + "A terminal RPG adventure\n")
    while True:
        print("1. Register\n2. Login\n3. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                Game(username).run()
        elif choice == "3":
            print("Farewell, adventurer!")
            break
        else:
            print(Fore.RED + "Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

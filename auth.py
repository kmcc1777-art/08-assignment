import hashlib
from colorama import Fore
from database import get_user, create_user

def _hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def register():
    print(Fore.CYAN + "\n--- Create account ---")
    username = input("Username: ").strip()
    if len(username) < 3 or not username.isalnum():
        print(Fore.RED + "Username must be at least 3 letters/numbers, with no spaces.")
        return
    if get_user(username):
        print(Fore.RED + "That username already exists.")
        return
    password = input("Password (at least 4 characters): ")
    if len(password) < 4:
        print(Fore.RED + "Password is too short.")
        return
    create_user({
        "username": username,
        "password_hash": _hash(password),
        "level": 1, "xp": 0, "gold": 25, "hp": 30, "max_hp": 30,
        "inventory": ["Potion", "Potion"], "skills": ["Strike"],
        "map": "village", "position": [1, 1],
        "quest": {"main": 0, "herbs": False, "wolf": False},
        "won": False
    })
    print(Fore.GREEN + "Account created! You can now log in.")

def login():
    print(Fore.CYAN + "\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ")
    user = get_user(username)
    if not user or user["password_hash"] != _hash(password):
        print(Fore.RED + "Incorrect username or password.")
        return None
    print(Fore.GREEN + f"Welcome back, {username}!")
    return username

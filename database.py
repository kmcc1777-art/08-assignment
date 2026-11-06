from tinydb import TinyDB, Query
from copy import deepcopy

DB = TinyDB("rpg_data.json")
USERS = DB.table("users")

def get_user(username):
    row = USERS.get(Query().username == username)
    return deepcopy(row) if row else None

def create_user(data):
    USERS.insert(data)

def save_user(username, data):
    USERS.update(data, Query().username == username)

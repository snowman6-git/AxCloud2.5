import os

KEY = os.path.join(os.path.dirname(__file__), "..", "key")

def secret_key():
    try:
        with open(f"{KEY}/ax25.txt") as value: return value.read()
    except:
        with open(f"{KEY}/example.txt") as value: return value.read()


import json
from cryptography.fernet import Fernet
import re

with open("keygen/key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Ok"
    else:
        return "Weak"

def generate_password(site, username):
    if not site or not username:
        print("Site and username cannot be empty.")
        return
    
    import random
    import string
    
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"Generated password for {site} ({username}): {password}")
    add_password(site, username, password)

def add_password(site, username, password):
    if not site or not username or not password:
        print("Site, username, and password cannot be empty.")
        return
    strength = check_password_strength(password)
    if strength == "Weak":
        print("Password is too weak. Please choose a stronger password.")
        return
    encrypted_password = fernet.encrypt(password.encode()).decode()
    
    entry = {
        "site": site,
        "username": username,
        "password": encrypted_password
    }
    ensure_file_exists()
    
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(entry)
    
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)
    print(f"Password for {site} added successfully.")

def view_password():
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            for entry in data:
                decrypted_password = fernet.decrypt(entry["password"].encode()).decode()
                print(f"Site: {entry['site']}, Username: {entry['username']}, Password: {decrypted_password}")
    except FileNotFoundError:
        print("No passwords saved yet.")

def search_password(site):
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            for entry in data:
                if entry["site"] == site:
                    decrypted_password = fernet.decrypt(entry["password"].encode()).decode()
                    print(f"Site: {entry['site']}, Username: {entry['username']}, Password: {decrypted_password}")
                    return
            print("No entry found for that site.")
    except FileNotFoundError:
        print("No passwords saved yet.")

def delete_password(site):
    if not site:
        print("Site cannot be empty.")
        return
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No passwords saved yet.")
        return
    
    new_data = [entry for entry in data if entry["site"] != site]
    
    if len(new_data) < len(data):
        with open("passwords.json", "w") as file:
            json.dump(new_data, file, indent=4)
        print(f"Entry for {site} deleted.")
    else:
        print(f"No entry found for {site}.")

def ensure_file_exists():
    try:
        with open("passwords.json", "x") as file:
            json.dump([], file, indent=4)
    except FileExistsError:
        pass
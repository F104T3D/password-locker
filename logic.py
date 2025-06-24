import json
from cryptography.fernet import Fernet

with open("keygen/key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

def add_password(site, username, password):
    if [site, username, password] is not None:
        print("valid input. saving...")
        encrypted_password = fernet.encrypt(password.encode()).decode()
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        data.append({"site": site, "username": username, "password": encrypted_password})
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)

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
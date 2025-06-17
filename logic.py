import json


def add_password(site, username, password):
    if [site, username, password] is not None:
        print("valid input. saving...")
        data = [
            {"site": site, "username": username, "password": password},
        ]
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)

def view_password():
    choice = int(input("Choose an option (1-5): ").strip())

    if choice == 1:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            print(data)

def search_password(site):
    with open("passwords.json", "r") as file:
        data = json.load(file)
        for entry in data:
            if entry["site"] == site:
                print(f"Site: {entry['site']}, Username: {entry['username']}, Password: {entry['password']}")
                return
        print("No entry found for that site.")

def delete_password(site):
    if not site:
        print("Site cannot be empty.")
        return
    with open("passwords.json", "r") as file:
        data = json.load(file)
    
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
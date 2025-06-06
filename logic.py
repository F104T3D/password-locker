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
    print("[1] All")
    choice = int(input("Choose an option (1-5): ").strip())

    if choice == 1:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            print(data)

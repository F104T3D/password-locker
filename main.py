import logic

try:
    with open("keygen/key.key", "rb") as key_file:
        key = key_file.read()
        print("[+] Key found. Proceeding with the program...")
except FileNotFoundError:
    from keygen import generator
    print("[!] Key not found. Generating a new key...")
    generator.generate_key()
    print("[+] Key generated successfully. Restarting the program.")
    exit()

while True:
    print("[1] Add new password\n[2] View all entries \n[3] Search by site\n[4] Delete an entry\n"
    "[5] Generate password\n[6] Exit")
    
    try:
        choice = int(input("Choose an option (1-6): ").strip())
    except ValueError:
        print("Input a number.")
        continue
    
    if choice == 1:
        site = input("site: ").strip()
        user = input("username or email: ")
        pword = input("password: ").strip()
        logic.add_password(site, user, pword)
    elif choice == 2:
        print("[1] All")
        logic.view_password()
    elif choice == 3:
        siteinp = input("site: ")
        logic.search_password(siteinp)
    elif choice == 4:
        siteinp = input("site: ")
        logic.delete_password(siteinp)
    elif choice == 5:
        site = input("site: ").strip()
        user = input("username or email: ")
        logic.generate_password(site, user)
    elif choice == 6:
        print("Goodbye.")
        break
import logic

while True:
    print("[1] Add new password\n[2] View all entries \n[3] Search by site\n[4] Delete an entry\n[5] Exit")
    
    try:
        choice = int(input("Choose an option (1-5): ").strip())
    except ValueError:
        print("Input a number.")
        continue
    
    if choice == 1:
        site = input("site: ").strip()
        user = input("username or email: ")
        pword = input("password: ").strip()
        logic.add_password(site, user, pword)
    elif choice == 2:
        logic.view_password()
    elif choice == 3:
        print("holder")
    elif choice == 4:
        print("holder")
    elif choice == 5:
        print("Goodbye.")
        break
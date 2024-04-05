from login import read_passwords

def read_users():
    users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, role = line.strip().split(",")
                users.append({'username': username, 'role': role})
    except FileNotFoundError:
        print("Error: Users file not found.")
    return users

def write_users(users):
    try:
        with open("users.txt", "w") as file:
            for user in users:
                file.write(f"{user['username']},{user['role']}\n")
        print("User records updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def write_passwords(passwords):
        with open("passwords.txt", "w") as file:
            for item in passwords:
                file.write(f"{item['username']},{item['password']}\n")
        print("Passwords updated successfully.")

def register_user():
    users = read_users()
    passwords = read_passwords()
    username = input("Enter username for new user: ")
    role = 'student'
    password = input('Enter password: ')
    users.append({'username':username, 'role':role})
    passwords.append({'username': username, 'password': password})
    write_users(users)
    write_passwords(passwords)

def modify_user():
    users = read_users()
    username = input("Enter username of user to modify: ")
    for user in users:
        if user['username'] == username:
            new_role = input("Enter new role for the user (admin/student): ")
            user['role'] = new_role
            write_users(users)
            print(f"Role for user '{username}' updated successfully.")
            return
    print("User not found.")

def delete_user():
    users = read_users()
    passwords = read_passwords()
    username = input("Enter username of user to delete: ")

    # Remove user from the users list
    for user in users:
        if user['username'] == username:
            users.remove(user)
            break
    else:
        print("User not found.")
        return

    # Remove password from the passwords dictionary
    for user in passwords:
        if user['username'] == username:
            passwords.remove(user)
            write_passwords(passwords)
            write_users(users)
            print(f"User '{username}' deleted successfully.")
        else:
            print("Password not found.")
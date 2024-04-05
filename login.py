def read_users():
    #users: [{username, role}]
    users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, role = line.strip().split(",")
                users.append({'username': username, 'role': role})
    except FileNotFoundError:
        print("Error: Users file not found.")
    return users

def read_passwords():
    #password: [{username, password}]
    passwords = []
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                passwords.append({'username': username, 'password': password})
    except FileNotFoundError:
        print("Error: Passwords file not found.")
    return passwords

def login_user():
    users = read_users()
    passwords = read_passwords()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        for authUser in passwords:
            if authUser['username'] == username and authUser['password'] == password:
                for user in users:
                    if user['username'] == username:
                        return user
                break
        else:
            print("Invalid username or password. Please try again.")

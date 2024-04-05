from login import read_users

def write_users(users):
    try:
        with open("users.txt", "w") as file:
            for user in users:
                file.write(f"{(user['username'].lower())},{user['role']}\n")
        print("User records updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def update_profile(username):
    users = read_users()
    for user in users:
        if user['username'] == username:
            role = input('update user role: ')
            user['role'] = role
            write_users(users)
            print("Profile updated successfully.")
            return
    print("User not found.")

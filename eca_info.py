def read_eca():
    eca_details = []
    try:
        with open("eca.txt", "r") as file:
            for line in file:
                username, activity, duration = line.strip().split(",")
                eca_details.append({'username': username, 'activity': activity, 'duration': duration})
    except FileNotFoundError:
        print("Error: ECA file not found.")
    return eca_details

def write_eca(eca_details):
    try:
        with open("eca.txt", "w") as file:
            for eca in eca_details:
                file.write(f"{eca['username']},{eca['activity']},{eca['duration']}\n")
        print("ECA records updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def view_eca(username):
    eca_details = read_eca()
    for eca in eca_details:
        if eca['username'] == username:
            print(f"Activity: {eca['activity']}, Duration: {eca['duration']}")
    print("End of ECA details.")

def update_eca(username):
    eca_details = read_eca()
    activity = input('new activity: ')
    for eca in eca_details:
        if eca['username'] == username:
            new_duration = input(f"Enter new duration for {activity}: ")
            eca['activity'] = activity
            eca['duration'] = new_duration
            write_eca(eca_details)
            print("ECA details updated successfully.")
            return
    print("ECA details not found.")

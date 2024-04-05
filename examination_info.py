def read_grades():
    #User,Marks_Maths,Marks_English,Marks_History,Marks_Computer,Marks_Science
    grades = []
    try:
        with open("grades.txt", "r") as file:
            for line in file:
                username, maths, english, history, computer, science = line.strip().split(",")
                grades.append({'username': username, 'maths': maths, 'english': english, 'history': history, 'computer': computer, 'science': science})
    except FileNotFoundError:
        print("Error: Grades file not found.")
    return grades

def write_grades():
    grades = read_grades()
    print("enter student's name and grades")
    username = input('student name: ')
    maths = input('maths: ')
    english = input('english: ')
    history = input('history: ')
    computer = input('computer: ')
    science = input('science: ')
    try:
        grades.append({'username': username, 'maths': maths, 'english': english, 'history': history, 'computer': computer, 'science': science})
        with open("grades.txt", "w") as file:
            for grade in grades:
                file.write(f"{grade['username']},{grade['maths']},{grade['english']},{grade['history']},{grade['computer']},{grade['science']}\n")
        print("Grade records updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def view_grades(username):
    grades = read_grades()
    for grade in grades:
        if grade['username'] == username:
            print(f"Student: {grade['username']}: \nMaths: {grade['maths']}\nEnglish: {grade['english']}\nHistory: {grade['history']}\ncomputer: {grade['computer']}\nscience: {grade['science']}")
    print("End of grades.")

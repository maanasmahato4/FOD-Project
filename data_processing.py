from examination_info import read_grades

def generate_grade_statistics(username):
    #User,Marks_Maths,Marks_English,Marks_History,Marks_Computer,Marks_Science
    marks = 0
    try:
       grades = read_grades()
       for grade in grades:
        if(grade['username'] == username):
           marks = int(grade['maths']) + int( grade['english']) + int(grade['history']) + int(grade['computer']) + int(grade['science'])
           average_marks = float((marks / 500) * 100)
        print("Grade statistics:")
        print(f"Aggregated marks: {average_marks}%")
        return
    except FileNotFoundError:
        print("Error: Grades file not found.")

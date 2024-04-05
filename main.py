from login import login_user
from user_management import register_user, modify_user, delete_user
from profile_management import update_profile
from examination_info import view_grades, write_grades
from eca_info import view_eca, update_eca
from data_processing import generate_grade_statistics

def main():
    # Login user
    print("welcome!\n Type L/l to login or R/r for new Registration")
    logOrRegister = input('')
    if(logOrRegister.lower() == 'r'):
        register_user()

    elif(logOrRegister.lower() == 'l'):
        user = login_user()
        flag = True
        optionValue = ''

        if user is None:
            print("Login failed. Exiting program.")
            return
        if user:
            print("choose your options:\nView your grades [type: A/a]\nView your aggregate marks [type: B/b]\nView ECA [type: E/e]\nUpdate ECA [type: U/u]\nUpdate Profile [type: P/p]\nClose App [type: C/c]\n")
            if(user['role'] == 'admin'): 
                print("Write grades [type: G/g]\nModify User [type: M/m]\nDelete User [type: D/d]")
            while flag:
                option = input('')
                optionValue = option
                if(optionValue.lower() == 'a'):
                    view_grades(user['username'])
                elif(optionValue.lower() == 'b'):
                    generate_grade_statistics(user['username'])
                elif(optionValue.lower() == 'c'):
                    flag = False
                    break
                elif(optionValue.lower() == 'e'):
                    view_eca(user['username'])
                elif(optionValue.lower() == 'u'):
                    update_eca(user['username'])
                elif(optionValue.lower() == 'p'):
                    update_profile(user['username'])
                elif(user['role'] == 'admin' and optionValue.lower() == 'm'):
                    modify_user()
                elif(user['role'] == 'admin' and optionValue.lower() == 'd'):
                    delete_user()
                elif(user['role'] == 'admin' and optionValue.lower() == 'g'):
                    write_grades()
                else:
                    print('error')
                    break
    else:
        print('error')

if __name__ == "__main__":
    main()

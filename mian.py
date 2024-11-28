from classes import *

def emp_menu(emp: Employee):
    message = f"""
Hello {emp.name}! Welcome back.
What do you wanna do today?
1. See your info
2. Change your info
""" 
    print(message)
    userIn = input("Type your choice: ")

    if userIn == '1':
        print(emp.get_info())
    elif userIn == '2':
        # Complete this at home!
        pass
    
    else:
        print("Wrong input, Try again!")

def man_menu(man: Super_Man):
    print(f"Hello {man.name}! welcome to managers' menu.")

def main():
    main_company = Company()
    main_manager = Super_Man("Erfan", "2002", "1500", main_company)
    main_manager.username = "Erfan"
    main_manager.password = "1234"
    main_company.add_emp(main_manager, "Manager")

    print("Welcome! Type your username and password.")

    while True:
        username = input("username: ")
        password = input("password: ")

        try:
            main_company.search_user(username, password)
        except ValueError as v:
            print(v)
            continue
        else:
            man_menu(main_manager)
            break

main()

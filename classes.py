class Employee:
    def __init__(self, name, birthyear, salary):
        self.name = name
        self.birthyear = birthyear
        self.salary = salary

    def set_user_pass(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

    def get_info(self):
        info = {
            "Name":self.name,
            "BirthYear":self.birthyear,
            "Salary":self.salary,
            "UserName":self.username
        }

    def change_info(self, username, name, birthyear):
        self.username = username
        self.name = name
        self.birthyear = birthyear


class Programmer(Employee):
    pass


class Tester(Employee):
    pass


class Manager(Programmer, Tester):
    pass

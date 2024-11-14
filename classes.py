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
    def get_all_projs(self, company):
        return company.get_all_projs()
    
    def add_proj(self, company, proj):
        company.add_proj(proj)
    
    def remove_proj(self, company, proj):
        company.remove_proj(proj)






class Tester(Employee):
    def accept_proj(self, company, proj):
        for p in company.projs:
            if p[0] == proj:
                p[1] = True

    def decline_proj(self, company, proj):
        for p in company.projs:
            if p[0] == proj:
                p[1] = False






class Manager(Programmer, Tester):
    pass


class Company:
    def __init__(self):
        self.emps = {
            "Employees":[],
            "Programmers":[],
            "Testers":[],
            "Managers":[]
        }
        self.projs = []

    def add_emp(self, emp, role):
        self.emps[role].append(emp)

    def remove_emp(self, emp, role):
        self.emps[role].remove(emp)

    def get_all_emps(self):
        return self.emps

    def add_proj(self, proj):
        self.projs.append(proj)

    def remove_proj(self, proj):
        self.projs.remove(proj)

    def get_all_projs(self):
        return self.projs



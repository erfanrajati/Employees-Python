class Employee:
    def __init__(self, name, birthyear, salary, company):
        self.name = name
        self.birthyear = birthyear
        self.salary = salary
        self.company = company

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
    def get_all_projs(self):
        return self.company.get_all_projs()
    
    def add_proj(self, proj):
        self.company.add_proj(proj)
    
    def remove_proj(self, proj):
        self.company.remove_proj(proj)



class Tester(Employee):
    def accept_proj(self, proj):
        for p in self.company.projs:
            if p[0] == proj:
                p[1] = True

    def decline_proj(self, proj):
        for p in self.company.projs:
            if p[0] == proj:
                p[1] = False




class Super_Man(Programmer, Tester):
    def add_emp(self, name, birth, salary, role):
        if role == "Employee":
            new_emp = Employee(name, birth, salary, self.company)
        
        if role == "Programmer":
            new_emp = Programmer(name, birth, salary, self.company)
        
        if role == "Tester":
            new_emp = Tester(name, birth, salary, self.company)
        
        if role == "Manager":
            new_emp = Super_Man(name, birth, salary, self.company)
        
        self.company.add_emp(new_emp, role)

    def remove_emp(self, emp, role):
        self.company.remove_emp(emp, role)

    def get_all_emps(self):
        return self.company.get_all_emps()


class Company:
    def __init__(self):
        self.emps = {
            "Employee":[],
            "Programmer":[],
            "Tester":[],
            "Manager":[]
        }
        self.projs = []

    def search_user(self, username, password):
        for role, emps in self.emps.items():
            for emp in emps:
                if emp.login(username, password):
                    return (role, emp)
        raise ValueError("Username or Password was wrong!")

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



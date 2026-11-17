class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def show_salary(self):
        print("Salary =", self.__salary)


e = Employee(30000)
e.show_salary()

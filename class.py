class Employee:

    emp_count = 0

    def __init__(self, name, salary) : # using self to refer to a specific
        self.name = name               # Employee
        self.salary = salary
        Employee.emp_count += 1

    def display_employee(self) :
        print("Name: %s, salary: %s" % (self.name, self.salary))

    def give_raise(self, percent) :
        self.salary += self.salary * percent

    def display_count(self) :
        print('count: %d' % Employee.emp_count)

emp = Employee("Sam", 1000)
emp.display_employee()
emp.give_raise(0.1)
empself.display_employee()

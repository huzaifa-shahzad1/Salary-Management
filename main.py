class Employee:
    def __init__(self):
        self.name = None
        self.age = None
        self.employee_id = None
        self.salary = None
        self.leaves = None
        self.month = None
        self.finalSalary = None

    def Employee(self):
        self.name = "NONE"
        self.age = 18
        self.employee_id = "DUMMY"
        self.salary = 10000
        self.leaves = 0
        self.month = "None"
        self.finalSalary = 10000

    def getInformation(self):
        self.name = input("Enter Name:  ")
        self.age = int(input("Enter Age:  "))
        self.employee_id = input("Enter ID:  ")
        self.salary = int(input("Enter Salary:  "))
        self.month = input("Enter the Month:  ")
        self.leaves = int(input(f"Enter the Number of Leaves in  {self.month}:  "))

    def calculateSalary(self):
        self.finalSalary = self.salary - (self.leaves * 500)

    def display(self):
        print(f"Name:  {self.name}")
        print(f"Age:  {self.age}")
        print(f"ID:  {self.employee_id}")
        print(f"Basic Salary:  {self.salary}")
        self.calculateSalary()
        print(f"Salary after {self.leaves} leaves in {self.month}:  {self.finalSalary}")


emp = []

for i in range(2):
    print(f"Enter the Information of Employee {i+1}")
    temp = Employee()
    temp.getInformation()
    emp.append(temp)

for i in range(2):
    emp[i].display()


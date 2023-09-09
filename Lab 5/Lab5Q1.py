class Employee:
    def __init__(self,idno,name,salary,department):
        self.idno= idno
        self.name= name
        self.salary=salary
        self.department = department
        self.emp_details=(idno,name,salary,department)

    def searchRecord(idno,employeelist):
        for employee in employeelist:
            if employee[0]==idno:
                print("ID:",employee[0])
                print("Name:",employee[1])
                print("Salary:",employee[2])
                print("Department:",employee[3])
            else:
                print("Employee not found!")
                


employeelist=[]
no_of_employees = int(input("Enter the number of employees:"))
for i in range(0,no_of_employees):
    print("--------------------------------------------------")
    idno = int(input("Enter the ID number of the employee:"))
    name = input("Enter the name of the employee:")
    salary = int(input("Enter the salary of the employee:"))
    department = input("Enter the name of the department:")
    eachemployee = Employee(idno,name,salary,department).emp_details
    employeelist.append(eachemployee)

print("The employee list is:",employeelist)

searchIdno= int(input("Enter the Employee ID of the employee to be searched:"))
Employee.searchRecord(searchIdno,employeelist)

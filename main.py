from PyBank import *


bank = Bank("Banca Transilvania")
employee_1 = Employee("Popescu", "Ion", "1234567890123", JobPerm.Manager)
bank.register_employee(employee_1)

employee_2 = Employee("Ionescu", "Maria", "9876543210987", JobPerm.Operator)
bank.register_employee(employee_2)

employee_3 = Employee("Vasilescu", "Ion", 456789123,JobPerm.Operator)
employee_4 = Employee("Georgescu", "Elena", 321654987,JobPerm.Operator)
employee_5 = Employee("Mihaescu", "Marin", 654987321,JobPerm.Operator)
employee_6 = Employee("Mihaescu", "Marin", 654987321,JobPerm.Operator)




bank.register_employee(employee_3)
bank.register_employee(employee_4)
bank.register_employee(employee_5)
bank.register_employee(employee_6)

bank.print_all_employee()
print("---")
bank.unregister_employee(employee_3.cnp)

bank.print_all_employee()
print("---")




employee_1 = Employee("Ionescu", "Cristian",3216123547,JobPerm.Operator)

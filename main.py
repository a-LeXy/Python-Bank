from PyBank import *
import logging
logging.basicConfig(level = logging.DEBUG, handlers = [logging.FileHandler("log.txt"), logging.StreamHandler()])

bank = Bank("Banca Transilvania")
employee_1 = Employee("Popescu", "Ion", 1234567890123, JobPerm.Manager)
employee_2 = Employee("Ionescu", "Maria", 9876543210987, JobPerm.Operator)
employee_3 = Employee("Vasilescu", "Ion", 456789123, JobPerm.Operator)
employee_4 = Employee("Georgescu", "Elena", 321654987, JobPerm.Operator)
employee_5 = Employee("Mihaescu", "Marin", 654987321, JobPerm.Operator)
employee_6 = Employee("Mihaescu", "Marin", 654987321, JobPerm.Operator)
bank.register_employee(employee_1)
employee_1.print_details()
bank.register_employee(employee_2)
employee_2.print_details()
bank.register_employee(employee_3)
employee_3.print_details()
bank.register_employee(employee_4)
employee_4.print_details()
bank.register_employee(employee_5)
employee_5.print_details()
bank.register_employee(employee_6)
employee_6.print_details()
# bank.print_all_employee()
# print("---")
# bank.unregister_employee(employee_3.cnp)
#
# bank.print_all_employee()
# print("---")
#
# bank.generate_report()
def read_persons():
    persoane = ""
    with open("Persoane.txt", 'r') as file:
        persoane = file.readlines()
        for p in persoane:
            p = p.split(",")
            p = Employee(p[0].strip(), p[1].strip(), p[2].strip(), JobPerm.Operator)
            bank.register_employee(p)
read_persons()
bank.generate_report()
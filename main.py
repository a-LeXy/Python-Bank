from PyBank import *


bank = Bank("Banca Transilvania")

persoana_1 = Person("Ionescu", "Cristi", 123456789)
persoana_2 = Person("Popescu", "Maria", 987654321)
persoana_3 = Person("Vasilescu", "Ion", 456789123)
persoana_4 = Person("Georgescu", "Elena", 321654987)
persoana_5 = Person("Mihaescu", "Marin", 654987321)


bank.register_employee(persoana_1)
bank.register_employee(persoana_2)
bank.register_employee(persoana_3)
bank.register_employee(persoana_4)
bank.register_employee(persoana_5)

bank.print_all_employee()
print(f"---")
bank.unregister_employee(persoana_3.cnp)

bank.print_all_employee()
print(f"---")

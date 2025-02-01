class Person:
    def __init__(self, nume , prenume, cnp):
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp
    def print_details(self):
        print(f"Nume: {self.nume} Prenume: {self.prenume} CNP {self.cnp}")

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.archive = []
    def register_employee(self, person):
        for existing_person in self.archive:
            if person.cnp == existing_person.cnp:
                print("Error: Existing Person can't be added")
                return
        self.archive.append(person)
    def unregister_employee(self, cnp):
        for p in self.archive:
            if p.cnp == cnp:
                self.archive.remove(p)

    def print_all_employee(self):
        for i in self.archive:
            i.print_details()




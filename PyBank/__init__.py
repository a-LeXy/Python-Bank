from enum import Enum

class JobPerm(Enum):
    Manager = 1
    Operator = 2
    Contabil = 3
    Programator = 4
    Secretar = 5
    Asistenta = 6
    Doctor = 7
    Mecanic = 8

class Utilitati:
    @staticmethod
    def print_banner(text):
        lunigme_baner = 60
        lungimea_textului = len(text)
        numar_spatii_goale = (lunigme_baner - lungimea_textului -3)
        print("-" * lunigme_baner)
        print(f"| {text}" + " " * numar_spatii_goale + "|")
        print("-" * lunigme_baner)



class Person:
    def __init__(self, nume , prenume, cnp):
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp
    def print_details(self):
        print(f"Nume: {self.nume} Prenume: {self.prenume} CNP {self.cnp}")

class Employee(Person):
    def __init__(self, nume , prenume, cnp, job):
        super().__init__(nume , prenume, cnp)
        self.job = job

    def print_my_job(self):
        print(f"Jobul acestui angajat este: {self.job}")




class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.archive = []
        self.jobs_available = [JobPerm.Manager, JobPerm.Operator, JobPerm.Contabil, JobPerm.Programator,
                               JobPerm.Secretar, JobPerm.Asistenta, JobPerm.Doctor, JobPerm.Mecanic]

    def check_jobs(self,employee):
        if employee.job in self.jobs_available:
            return True
        else:
            return False
            Utilitati.print_banner(f"Job not available {empolyee.job}")

    def check_employee(self,employee):
        if not self.check_jobs(employee):
            return False
        for existing_person in self.archive:
            if employee.cnp == existing_person.cnp:
                Utilitati.print_banner("Error: Existing Person can't be added")
                return False
        return True


    def register_employee(self,employee):
        if self.check_employee(employee):
            self.archive.append(employee)

    def unregister_employee(self, cnp):
        for p in self.archive:
            if p.cnp == cnp:
                self.archive.remove(p)

    def print_all_employee(self):
        for i in self.archive:
            i.print_details()







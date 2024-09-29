class Job:
    def __init__(self, title, salary_range):
        self.title = title
        self.salary_range = salary_range

    def __str__(self):
        return f"{self.title}, Salary Range: {self.salary_range}"

class TaxCollection:
    def __init__(self, federal_tax, state_tax, local_tax):
        self.federal_tax = federal_tax
        self.state_tax = state_tax
        self.local_tax = local_tax

    def calculate_total_tax(self):
        return self.federal_tax + self.state_tax + self.local_tax

    def __str__(self):
        return f"Federal Tax: {self.federal_tax}, State Tax: {self.state_tax}, Local Tax: {self.local_tax}"

class Salary:
    def __init__(self, base_salary, tax_collection):
        self.base_salary = base_salary
        self.tax_collection = tax_collection

    def calculate_net_salary(self):
        total_tax = self.tax_collection.calculate_total_tax()
        return self.base_salary - total_tax

    def __str__(self):
        net_salary = self.calculate_net_salary()
        return f"Base Salary: {self.base_salary}, Net Salary: {net_salary}"

class Employee:
    def __init__(self, name, employee_id, job, base_salary, tax_collection):
        self.name = name
        self.employee_id = employee_id
        self.job = job  # Aggregation
        self.salary = Salary(base_salary, tax_collection)  # Aggregation

    def __str__(self):
        return f"Employee: {self.name}, Job: {self.job.title}, {self.salary}"

class Reportee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, employee_id, job, base_salary, tax_collection):
        super().__init__(name, employee_id, job, base_salary, tax_collection)
        self.reportees = []  # Composition 

    def add_reportee(self, name):
        reportee = Reportee(name)
        self.reportees.append(reportee)

    def __str__(self):
        reportee_names = ", ".join(reportee.name for reportee in self.reportees)
        return f"Manager: {self.name}, Reportees: [{reportee_names}], {self.salary}"

software_engineer = Job("Software Engineer", (60000, 120000))
manager_job = Job("Manager", (80000, 160000))

tax_collection1 = TaxCollection(federal_tax=10000, state_tax=5000, local_tax=2000)
tax_collection2 = TaxCollection(federal_tax=12000, state_tax=6000, local_tax=2500)

employee1 = Employee("Rama", 1, software_engineer, 70000, tax_collection1)
employee2 = Employee("Sita", 2, software_engineer, 80000, tax_collection1)

manager = Manager("Cal", 3, manager_job, 90000, tax_collection2)
manager.add_reportee("David")
manager.add_reportee("Ermias")


print(employee1)
print(employee2)
print(manager)

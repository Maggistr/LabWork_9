class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        print(f"{self.name} c айди {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        print(f'Типо работай человек с таким именем {self.name} с таким айди {self.emp_id} из такого отдела {self.department}')


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        print(f'{self.name} запускает техническое обслуживание.')


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)

        self.team = []

    def add_employee(self, name, emp_id):
       self.team.append(Employee(name, emp_id))
       print(f"Добавлен сотрудник:{name}, его aйди {emp_id}")

    def team_info(self):
        for peaple in self.team:
            print(peaple.get_info())


employee = Employee("ABC", 123)
technician = Technician("DEF", 456, "asfd")
manager = Manager("GHI", 789, "sdf")
tech_manager = TechManager("XYZ", 10, "SAD", "SDFSFDFSD")

print(tech_manager.add_employee(employee.name, employee.emp_id))

print(tech_manager.team_info())

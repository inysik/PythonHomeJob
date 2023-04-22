from logger import Logger
from operation import Operation

class Controller:
    def __init__(self):
        self.logger = Logger()
        self.operation = Operation()

    def add_employee(self, name, salary):
        self.operation.add_employee(name, salary)
        self.logger.log(f'Добавлен сотрудник {name} с зарплатой {salary}')

    def remove_employee(self, id):
        self.operation.remove_employee(id)
        self.logger.log(f'Удален сотрудник с id {id}')

    def update_employee(self, id, field, value):
        self.operation.update_employee(id, field, value)
        self.logger.log(f'Обновлено поле {field} для сотрудника с id {id}')

    def list_employees(self):
        employees = self.operation.list_employees()
        for employee in employees:
            print(employee)

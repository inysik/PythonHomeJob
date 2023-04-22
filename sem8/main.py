from controller import Controller

def main():
    controller = Controller()

    while True:
        print('Выберите действие:')
        print('1. Добавить сотрудника')
        print('2. Удалить сотрудника')
        print('3. Обновить данные сотрудника')
        print('4. Получить список сотрудников')
        print('5. Выход')

        choice = input()

        if choice == '1':
            name = input('Введите имя сотрудника: ')
            salary = input('Введите зарплату сотрудника: ')
            controller.add_employee(name, salary)
        elif choice == '2':
            id = input('Введите id сотрудника: ')
            controller.remove_employee(id)
        elif choice == '3':
            id = input('Введите id сотрудника: ')
            field = input('Введите поле, которое нужно обновить: ')
            value = input('Введите новое значение: ')
            controller.update_employee(id, field, value)
        elif choice == '4':
            controller.list_employees()
        elif choice == '5':
            break
        else:
            print('Неправильный выбор')

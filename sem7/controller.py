from operation import load_data, save_data


class Controller:
    def __init__(self):
        self.entries = []
        self.operations = {
            'load': self.load,
            'save': self.save,
            'add': self.add_entry,
            'edit': self.edit_entry,
            'remove': self.remove_entry,
            'show': self.show_entries,
        }

    def load(self, file_name, file_type):
        self.entries = load_data(file_name, file_type)

    def save(self, file_name, file_type):
        save_data(file_name, file_type, self.entries)

    def add_entry(self):
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        self.entries.append({'name': name, 'phone': phone})

    def edit_entry(self):
        index = input('Enter index: ')
        if not index.isdigit():
            print('Invalid index')
            return
        index = int(index)
        if index < 0 or index >= len(self.entries):
            print('Index out of range')
            return
        name = input('Enter new name: ')
        phone = input('Enter new phone: ')
        self.entries[index] = {'name': name, 'phone': phone}

    def remove_entry(self):
        index = input('Enter index: ')
        if not index.isdigit():
            print('Invalid index')
            return
        index = int(index)
        if index < 0 or index >= len(self.entries):
            print('Index out of range')
            return
        del self.entries[index]

    def show_entries(self):
        for i, entry in enumerate(self.entries):
            print(f'{i}: {entry["name"]} {entry["phone"]}')

    def process_command(self, command):
        if command[0] not in self.operations:
            print('Invalid command')
            return
        if len(command) == 1:
            self.operations[command[0]]()
        elif len(command) == 3:
            self.operations[command[0]](command[1], command[2])
        else:
            print('Invalid command')
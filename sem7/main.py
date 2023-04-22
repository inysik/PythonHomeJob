from controller import Controller
from logger import Logger


def main():
    controller = Controller()
    logger = Logger()

    logger.log('Phonebook started')

    while True:
        command = input('> ').split()
        if command[0] == 'exit':
            break
        controller.process_command(command)

    logger.log('Phonebook stopped')


if __name__ == '__main__':
    main()
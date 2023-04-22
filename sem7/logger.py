import logging


LOG_FILE_NAME = 'phonebook.log'


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename=LOG_FILE_NAME)

    def log(self, message):
        logging.info(message)
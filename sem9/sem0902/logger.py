import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.DEBUG)

    def log(self, message):
        logging.info(message)

class Logger:
    def __init__(self):
        self.log_file = 'log.txt'

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

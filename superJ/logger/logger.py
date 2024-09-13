import logging

BASIC_FORMAT = '%(asctime)s(%(process)d-%(thread)d)[%(levelname)s] %(message)s'

class default_logger():
    def __init__(self,name:str=None):
        if name:
            self.logger = logging.getLogger(name)
        else:
            self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # default level is DEBUG
        formatter = logging.Formatter(BASIC_FORMAT)
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(formatter)
        self.logger.addHandler(self.console_handler)

    def set_logfile(self, filename):
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(logging.Formatter(BASIC_FORMAT))
        self.logger.addHandler(file_handler)

    def setLevel(self, level):
        self.logger.setLevel(level)

    def info(self, message):
        message = f'👉 {message}'
        self.logger.info(message)

    def warning(self, message):
        message = f'😥 {message}'
        self.logger.warning(message)

    def error(self, message):
        message = f'😡 {message}'
        self.logger.error(message)

    def debug(self, message):
        message = f'👀 {message}'
        self.logger.debug(message)

    def critical(self, message):
        message = f'😱 {message}'
        self.logger.critical(message)

    def exception(self, message):
        message = f'💥 {message}'
        self.logger.exception(message)

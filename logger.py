import logging

class CustomLogger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Failed to log info: {e}')  

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error(f'Failed to log warning: {e}') 

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f'Failed to log error: {e}') 

    def log_exception(self, message):
        try:
            self.logger.exception(message)
        except Exception as e:
            self.logger.error(f'Failed to log exception: {e}')
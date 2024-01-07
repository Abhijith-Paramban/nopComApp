import logging

class LogGen:
    @staticmethod
    def logGen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s [%(levelname)s] [%(module)s] - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
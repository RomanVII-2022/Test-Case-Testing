import logging


class LogGen:
    @staticmethod
    def log_gen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s : %(lineno)d : %(message)s')
        file_handler = logging.FileHandler('C:\\highbridselenium\\ecommerceApp\\logs\\test.log', 'w')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger
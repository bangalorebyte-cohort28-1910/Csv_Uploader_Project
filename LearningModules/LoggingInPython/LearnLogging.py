import model, view, settings

import logging

def learnLogging():

    username = "ABC User"
    errmsg = "INVALID PASSWORD"

    logging.basicConfig(level=logging.DEBUG, filename='xlsUploaderLog.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.DEBUG, filename='xlsUploaderLog.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(filename='xlsUploaderLog.log', filemode='w', format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    logging.info('Admin logged in')
    logging.basicConfig(level=logging.DEBUG)
    logging.info('ABC User trying to log in')
    logging.warning('This will get logged to a file')
    logging.warning(f'{username} Could not login because of {errmsg}')

def exceptionLogging():
    a = 5
    b = 0
    try:
        c = a / b
    except Exception as e:
        logging.exception("Exception occurred")
        logging.exception("Exception occurred", exc_info=True)

def loggingUsingHandlers():
    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('file.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.warning('This is a warning')
    logger.error('This is an error')


if __name__ == '__main__':
    learnLogging()
    exceptionLogging()
    loggingUsingHandlers()
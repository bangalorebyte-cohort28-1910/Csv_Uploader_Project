# from src.main.python import model, view, settings
import logging
import model, view, settings

logger = logging.getLogger('controller')

# Global Variable to store CSV dataframe
CSV_DF_OBJ = None


def validate_login(username:str, password:str):
    """
    This function reads the username & password 
    from the view and validates the user 
    @param username, password
    @return String ['VALID_USER' | 'INVAID_USERNAME' | 'INVALID_PASSWORD']
    """
    logger.debug('Executing method validate_login()')

    if username in settings.LOGIN_CREDENTIALS.keys():
        if password == settings.LOGIN_CREDENTIALS[username]:
            response = 'VALID_USER'
        else:
            response = 'INVALID_PASSWORD'
    else:
        response= 'INVAID_USERNAME'
    
    logger.debug(f'response :: {response}')
    logger.debug('Exiting method validate_login()')
    pass


def validate_csv():
    """
    This function uploads csv file & reads, through a dataframe object. 
    It captures the column names from file and compares with the static column list
    to check if the uploaded csv file is in the expected format.
    @param filename
    @return String ['VALID_CSV' | 'INVAID_CSV']
    """
    logger.debug('Executing method validate_csv()')

    # TODO 
    # if <csv format is correct>
    # CSV_DF_OBJ = <dataframe object>
    # global CSV_DF_OBJ

    logger.debug('Exiting method validate_csv()')
    pass

def send_csv():
    """
    If it is a valid column list, the dataframe object is sent to model.py
    to push the records and update database.
    @return String ['DB_UPDATE_SUCCESSFUL' | 'DB_UPDATE_FAILED']
    """
    logger.debug('Executing method send_csv()')

    # model.push_csv_records_to_db(CSV_DF_OBJ)

    logger.debug('Exiting method send_csv()')

    pass


def addnums(a, b):
    return a+b

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='csvUploaderLog.log', filemode='a', format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
    # validate_login('user123', 'password1234')
    view.openLoginWindow()
    # view.openCsvUploaderWindow()
    logging.debug('Exiting Application from __main__')
    logging.shutdown()
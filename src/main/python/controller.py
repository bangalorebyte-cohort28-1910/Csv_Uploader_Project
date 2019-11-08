import sys, os
sys.path.insert(1, os.path.dirname(__file__))
import model, view, settings
import logging
import pandas as pd


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
    return response


def validate_csv(file_name):
    """
    This function uploads csv file & reads, through a dataframe object. 
    It captures the column names from file and compares with the static column list
    to check if the uploaded csv file is in the expected format.
    @param filename
    @return String ['VALID_CSV' | 'INVAID_CSV']
    """
    logger.debug('Executing method validate_csv()')

    if (file_name.split(".")[1] == "csv"):
        df = pd.read_csv(file_name)
    else: 
        (file_name.split(".")[1] == "xlsx")
        df = pd.read_excel(file_name)

    df = df.drop(['Unnamed: 0'], axis=1)
    column_list = list(df.columns.values)
    if column_list == settings.COLUMNS_LIST:
        response = "VALID_CSV"

        global CSV_DF_OBJ
        CSV_DF_OBJ = df
    else:
        response = "INVALID_CSV"


    logger.debug(f'column list :: {str(column_list)}')
    logger.debug('Exiting method validate_csv()')
    return response


def send_csv():
    """
    If it is a valid column list, the dataframe object is sent to model.py
    to push the records and update database.
    @return String ['DB_UPDATE_SUCCESSFUL' | 'DB_UPDATE_FAILED']
    """
    logger.debug('Executing method send_csv()')

    dbresponse = model.push_csv_records_to_db(CSV_DF_OBJ)

    logger.debug('Exiting method send_csv()')

    return dbresponse


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='csvUploaderLog.log', filemode='a', format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
    
    # view.openLoginWindow()
    validate_csv_response = validate_csv('Sample_valid.csv')
    if(validate_csv_response == 'VALID_CSV'):
        send_csv()
    else:
        logger.error('INVALID_CSV :: csv file sent was invalid')

    logging.debug('Exiting Application from __main__')
    logging.shutdown()
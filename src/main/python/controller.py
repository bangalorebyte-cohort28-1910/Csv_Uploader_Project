import model, view, settings

# Global Variable to store CSV dataframe
CSV_DF_OBJ = None


def validate_login():
    """
    This function reads the username & password 
    from the view and validates the user 
    @param username, password
    @return String ['VALID_USER' | 'INVAID_USERNAME' | 'INVALID_PASSWORD']
    """
    pass


def validate_csv():
    """
    This function uploads csv file & reads, through a dataframe object. 
    It captures the column names from file and compares with the static column list
    to check if the uploaded csv file is in the expected format.
    @param filename
    @return String ['VALID_CSV' | 'INVAID_CSV']
    """

    # if <csv format is correct>
    # CSV_DF_OBJ = <dataframe object>
    # global CSV_DF_OBJ
    pass

def send_csv():
    """
    If it is a valid column list, the dataframe object is sent to model.py
    to push the records and update database.
    @return String ['DB_UPDATE_SUCCESSFUL' | 'DB_UPDATE_FAILED']
    """

    # model.push_csv_records_to_db(CSV_DF_OBJ)

    pass


def addnums(a, b):
    return a+b

if __name__ == '__main__':
    view.openLoginWindow()
    # view.openCsvUploaderWindow()
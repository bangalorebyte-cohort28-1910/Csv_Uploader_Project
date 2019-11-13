import sys, os, settings, logging
sys.path.insert(1, os.path.dirname(__file__))
from model import Model
from view import ViewLogin, ViewFileBrowseWindow, ViewUpdateDBWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd


logger = logging.getLogger('controller')

class Controller:

    def __init__(self):
        # Creating ViewLogin object
        self.login = ViewLogin()

        # Creating Model object
        self.modelobj = Model()

        # Variable to store CSV dataframe
        self.CSV_DF_OBJ = None

    def show_login(self):
        self.login = ViewLogin()
        self.login.switch_window.connect(self.handle_login)
        self.login.show()

    def show_window_file_browse(self):
        self.window_file_browse = ViewFileBrowseWindow()
        self.window_file_browse.switch_window.connect(self.handle_main_window)
        self.login.close()
        self.window_file_browse.show()

    def show_window_update_db(self, text):
        self.window_update_db = ViewUpdateDBWindow(text)
        self.window_update_db.switch_window.connect(self.handle_push_csv_data)
        self.window_file_browse.close()
        self.window_update_db.show()

    def validate_login(self, username:str, password:str):
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

    def handle_login(self):
        logger.debug("LGN_PWD :: " + self.login.username + " : " + self.login.password)
        validate_login_response = self.validate_login(self.login.username, self.login.password)
        logger.debug("validate_login_response :: " + validate_login_response)
        if(validate_login_response == "INVAID_USERNAME"):
            logger.debug("In handle_login()-validate_login_response == INVAID_USERNAME")
            self.login.show_error("Username is invalid. Please enter a valid Username and try again.")
            logger.debug("exiting if INVAID_USERNAME")
        elif(validate_login_response == "INVALID_PASSWORD"):
            logger.debug("In handle_login()-validate_login_response == INVAID_PASSWORD")
            self.login.show_error("Password is invalid. Please enter a valid Password and try again.")
            logger.debug("exiting elif INVAID_PASSWORD")
        else:
            logger.debug("In handle_login()-else")
            self.login.close()
            self.show_window_file_browse()
            logger.debug("exiting else")

    def validate_csv(self, file_name):
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
            self.CSV_DF_OBJ = df
        else:
            response = "INVALID_CSV"
            self.CSV_DF_OBJ = None

        logger.debug(f'column list :: {str(column_list)}')
        logger.debug('Exiting method validate_csv()')
        return response

    def handle_main_window(self):
        logger.debug("Absolute File name :: " + self.window_file_browse.absolute_filename)
        validate_csv_response = self.validate_csv(self.window_file_browse.absolute_filename)
        logger.debug("validate_csv_response :: " + validate_csv_response)
        if(validate_csv_response == "INVALID_CSV"):
            logger.debug("In handle_main_window()-validate_login_response == INVALID_CSV")
            self.window_file_browse.show_message("Selected File is invalid. Please enter a valid csv(.csv) or excel(.xlsx) file and try again.")
            logger.debug("exiting if INVALID_CSV")
        elif(validate_csv_response == "VALID_CSV"):
            logger.debug("In handle_main_window()-validate_login_response == VALID_CSV")
            self.window_file_browse.close()
            self.show_window_update_db(self.window_file_browse.absolute_filename)
            logger.debug("exiting elif VALID_CSV")
        else:
            logger.debug("In handle_main_window()-else")
            # self.login.close()
            # self.show_main()
            logger.debug("exiting else")

    def call_push_csv_records_to_db(self):
        """
        If it is a valid column list, the dataframe object is sent to model.py
        to push the records and update database.
        @return String ['DB_UPDATE_SUCCESSFUL' | 'DB_UPDATE_FAILED']
        """
        logger.debug('Executing method call_push_csv_records_to_db()')
        
        db_response = self.modelobj.push_csv_records_to_db(self.CSV_DF_OBJ)

        logger.debug('Exiting method call_push_csv_records_to_db()')

        return db_response

    def handle_push_csv_data(self):
        logger.debug("In handle_push_csv_data()")
        push_csv_data_response = self.call_push_csv_records_to_db()
        logger.debug("push_csv_data_response :: " + push_csv_data_response)
        if(push_csv_data_response == "DB_UPDATE_SUCCESSFUL"):
            logger.debug("In handle_push_csv_data()-push_csv_data_response == DB_UPDATE_SUCCESSFUL")
            self.window_update_db.show_update_db_message("Database has been updated successfully! \nThankyou for choosing CSV Uploader App! \nSee you again!")
            
            # timer = QtCore.QTimer()

            # def num():
            #     # global i, timer
            #     i=0
            #     if i < 10:
            #         print ( i )
            #     else:
            #         timer.stop()
            #     i += 1

            # timer.timeout.connect(num)
            # timer.start(2000)

            self.window_file_browse.close()
            logger.debug("exiting if DB_UPDATE_SUCCESSFUL")
        elif(push_csv_data_response == "DB_UPDATE_FAILED"):
            logger.debug("In handle_push_csv_data()-push_csv_data_response == DB_UPDATE_FAILED")
            self.window_update_db.show_update_db_message("Problem occurred while pushing data to database. Could not update database. Please try again!")
            logger.debug("exiting elif DB_UPDATE_FAILED")
        else:
            logger.debug("In handle_push_csv_data()-else")
            logger.debug("This is an unexpected condition...")
            logger.debug("exiting else")
        

def main():
    app = QtWidgets.QApplication(sys.argv)

    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(3, 18, 14))
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # Setting logger to use current filename
    logging.basicConfig(level=logging.DEBUG, filename='csvUploaderLog.log', filemode='a', format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')

    main()

    logging.debug('Exiting Application from __main__')
    logging.shutdown()
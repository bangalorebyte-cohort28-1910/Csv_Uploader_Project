import sys, logging, settings
from model import Model
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt
import pandas as pd

    
logger = logging.getLogger(__name__)

class ViewFileBrowseWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Csv Uploader - Step 1 of 2 [Browse & Validate spreadsheet file]')
        self.setGeometry(QtCore.QRect(450, 450, 800, 200))

        # Set initial class variables
        self.absolute_filename = ""

        layout = QtWidgets.QVBoxLayout()

        layout_filebrowse = QtWidgets.QGridLayout()

        self.filelabel = QtWidgets.QLabel("Select File : ")
        layout_filebrowse.addWidget((self.filelabel), 0, 0)

        self.line_edit_filename = QtWidgets.QLineEdit()
        layout_filebrowse.addWidget((self.line_edit_filename), 0, 1)

        self.button_browse = QtWidgets.QPushButton('Browse')
        self.button_browse.clicked.connect(self.open_file_dialog)
        layout_filebrowse.addWidget((self.button_browse), 0, 2)

        self.button_validate_excel = QtWidgets.QPushButton('Validate Excel file')
        self.button_validate_excel.clicked.connect(self.call_validate_csv)
        layout_filebrowse.addWidget((self.button_validate_excel), 2, 1)

        layout_validation_message = QtWidgets.QHBoxLayout()

        self.label_validation_message = QtWidgets.QLabel()
        self.label_validation_message.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout_validation_message.addWidget(self.label_validation_message)

        layout.addLayout(layout_filebrowse)
        layout.addLayout(layout_validation_message)

        self.setLayout(layout)

        # Set window background color
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#B0D07F"))
        self.setPalette(p)
        self.setAutoFillBackground(True)


        self.show()

    def open_file_dialog(self):
        fileName, _ =QtWidgets.QFileDialog.getOpenFileName(None, 'Browse File', "c:\\","Csv File (*.csv);; Excel Files(*.xlsx)")
        self.line_edit_filename.setText(fileName)
        if fileName:
            logger.debug("Browsed File name :: " + fileName)
        else:
            logger.debug("User yet needs to Browse a File")
       

    def call_validate_csv(self):
        self.absolute_filename = self.line_edit_filename.text()
        if self.absolute_filename is '':
            logger.debug("Empty File name found :: ")
            QMessageBox.about(self,"Empty file path found","Please browse to select a valid file.")
        else:
            logger.debug("Selected File name :: " + self.absolute_filename)
            # QMessageBox.about(self,"Selected File","The selected file is  :: " + self.absolute_filename)
            self.switch_window.emit(self.line_edit_filename.text())

    def show_message(self, msg):
        logger.debug("In show_message()")
        logger.debug("Setting msg :: " + msg)
        self.label_validation_message.setText(msg)

    def switch(self):
        self.absolute_filename = self.line_edit.text()
        self.switch_window.emit(self.line_edit.text())


class ViewUpdateDBWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Csv Uploader - Step 2 of 2 [Push spreadsheet file data to Database]')
        self.setGeometry(QtCore.QRect(450, 450, 800, 200))

        layout = QtWidgets.QVBoxLayout()

        self.filelabel = QtWidgets.QLabel("Your Selected File : [ " + text + " ] data is ready to be pushed to Database. Would you like to like to push data to Database now? ")
        layout.addWidget(self.filelabel)
        
        layout_btn_row = QtWidgets.QHBoxLayout()
        self.btns_widget = QtWidgets.QWidget()
        layout_btn_options = QtWidgets.QHBoxLayout()

        self.button_push_data = QtWidgets.QPushButton('Push Spreadsheet Data to Database')
        self.button_push_data.clicked.connect(self.call_push_data_to_db)
        layout_btn_options.addWidget(self.button_push_data)

        self.button_later = QtWidgets.QPushButton('Will Update Later')
        self.button_later.clicked.connect(self.update_later)
        layout_btn_options.addWidget(self.button_later)

        self.btns_widget.setLayout(layout_btn_options)

        layout_btn_row.addWidget(self.btns_widget)

        layout.addLayout(layout_btn_row)

        layout_update_db_message = QtWidgets.QVBoxLayout()
        # self.final_widget = QtWidgets.QWidget()
        layout_exit_btn_grid = QtWidgets.QGridLayout()

        self.label_update_db_message = QtWidgets.QLabel()
        self.label_update_db_message.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout_update_db_message.addWidget(self.label_update_db_message)

        self.button_logout_exit = QtWidgets.QPushButton('Logout and Exit')
        self.button_logout_exit.clicked.connect(self.close_app)
        layout_exit_btn_grid.addWidget(QtWidgets.QLabel(), 0, 0)
        layout_exit_btn_grid.addWidget((self.button_logout_exit), 0, 1)
        layout_exit_btn_grid.addWidget(QtWidgets.QLabel(), 0, 2)

        # self.final_widget.setLayout(layout_final_display)
        self.button_logout_exit.hide()

        layout_update_db_message.addLayout(layout_exit_btn_grid)

        layout.addLayout(layout_update_db_message)

        layout.setContentsMargins(10, 10, 10, 10)


        self.setLayout(layout)

        # Set window background color
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#D5B3FF"))
        self.setPalette(p)
        self.setAutoFillBackground(True)

        self.show()

    def call_push_data_to_db(self):
        logger.debug("User chose to push data to DB")
        self.switch_window.emit()

    def update_later(self):
        logger.debug("User chose to Update Later")
        close_window = QMessageBox.question(self,"Update Later?","Do you really want to exit without updating database?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if close_window == QMessageBox.Yes:
            logger.debug("User chose to Exit. Hence closing window & exiting app without updating DB.")
            self.close()
        else:
            logger.debug("User chose to stay on this app maybe to update DB.")

    def show_update_db_message(self, msg):
        logger.debug("In show_update_db_message()")
        logger.debug("Setting msg :: " + msg)
        self.btns_widget.setDisabled(True)
        self.label_update_db_message.setText(msg)
        self.button_logout_exit.show()

    def close_app(self):
        logger.debug("Update Done! Exiting App")
        self.close()


class ViewLogin(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Csv Uploader - User Login')

        # Set initial class variables
        self.errormessage = ""
        self.username = ""
        self.password = ""

        # Set layout for Main Login Window
        layout = QtWidgets.QVBoxLayout()
        self.setGeometry(QtCore.QRect(450, 450, 800, 200))

        # Set layout for Login Credentials & add widgets
        layout_login = QtWidgets.QGridLayout()
        
        self.label_username = QtWidgets.QLabel("UserName :")
        self.label_password = QtWidgets.QLabel("Password :")

        self.text_username = QtWidgets.QLineEdit()
        self.text_username.setPlaceholderText("username")
        self.text_password = QtWidgets.QLineEdit()
        self.text_password.setPlaceholderText("password")

        layout_login.addWidget((self.label_username), 0, 0)
        layout_login.addWidget((self.text_username), 0, 1)
        layout_login.addWidget((self.label_password), 1, 0)
        layout_login.addWidget((self.text_password), 1, 1)

        # Set layout for Login Error message display & add widgets
        layout_errormessage = QtWidgets.QHBoxLayout()

        self.label_message = QtWidgets.QLabel()
        self.label_message.setText(self.errormessage)
        self.label_message.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        layout_errormessage.addWidget(self.label_message)
        
        # Set layout for Login buttons & add widgets
        layout_btns = QtWidgets.QHBoxLayout()

        self.button_login = QtWidgets.QPushButton('Login')
        self.button_cancel = QtWidgets.QPushButton('Cancel')

        self.button_login.clicked.connect(self.login)
        self.button_cancel.clicked.connect(self.check_cancel)

        layout_btns.addWidget(self.button_login)
        layout_btns.addWidget(self.button_cancel)

        # Adding to Main Login layout
        layout.addLayout(layout_login)
        layout.addLayout(layout_errormessage)
        layout.addLayout(layout_btns)

        layout.setContentsMargins(80, 80, 80, 80)

        self.setLayout(layout)

        # Set window background color
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#D2E3EE"))
        self.setPalette(p)
        self.setAutoFillBackground(True)
        
        # Set window to show up
        self.show()

    def login(self):
        self.username = self.text_username.text()
        self.password = self.text_password.text()
        self.switch_window.emit()

    def check_cancel(self):
        logger.debug("User chose to Exit")
        close_window = QMessageBox.question(self,"Close Window?","Do you really want to exit?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if close_window == QMessageBox.Yes:
            logger.debug("User chose to Exit. Hence closing window & exiting app.")
            self.close()
        else:
            logger.debug("User chose to stay on this app.")

    def show_error(self, msg):
        self.label_message.setText(msg)
        # pfg = self.palette()
        # pfg.setColor(self.foregroundRole(), QtGui.QColor("#ff010f"))
        # self.setPalette(pfg)
        # self.label_message.setForegroundRole(pfg)
        self.label_message.show()
    
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox 
import sys

def openLoginWindow():
    appctxt = ApplicationContext()
    login_dialog = QDialog()
    login_dialog.setWindowTitle('CSV Uploader User Login')
    login_dialog.setGeometry(250, 200, 400, 150)
    dlgLayout = QVBoxLayout()
    formLayout = QFormLayout()
    formLayout.addRow('Username:', QLineEdit())
    formLayout.addRow('Password:', QLineEdit())
    dlgLayout.addLayout(formLayout)
    btns = QDialogButtonBox()
    btn_Cancel = QDialogButtonBox.Cancel
    btn_Ok = QDialogButtonBox.Ok
    btns.setStandardButtons(btn_Cancel | btn_Ok)
    # btn_Ok.clicked.connect(openCsvUploaderWindow())
    dlgLayout.addWidget(btns)
    login_dialog.setLayout(dlgLayout)
    login_dialog.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)

def openCsvUploaderWindow():
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    window.setWindowTitle('CSV Uploader App')
    window.resize(450, 250)
    window.center()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
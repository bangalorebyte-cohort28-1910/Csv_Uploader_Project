import sys, os, unittest
sys.path.insert(1, os.path.dirname('controller.py'))
from src.main.python.controller import Controller
import pandas as pd
 
class TestController(unittest.TestCase):
 
    def setUp(self):
        self.df = pd.read_csv("Sample_valid.csv")
        self.df1 = pd.read_csv("Sample_invalid1.csv")
        self.controllerobj = Controller()


    def test_validateLogin(self):
        self.assertEqual(self.controllerobj.validate_login('username123', 'password1234'), "INVAID_USERNAME")
        self.assertEqual(self.controllerobj.validate_login('user123', 'password1234'), "INVALID_PASSWORD")
        self.assertEqual(self.controllerobj.validate_login('user123', 'password123'), "VALID_USER")
       

    def test_validateCSV(self):
        #self.assertEqual( controller.validate_csv(), True)
        self.assertEqual(self.controllerobj.validate_csv("Sample_invalid1.xlsx"), "INVALID_CSV")
        self.assertEqual(self.controllerobj.validate_csv("Sample_invalid2.xlsx"), "INVALID_CSV")
        self.assertEqual(self.controllerobj.validate_csv("Sample_valid.xlsx"), "VALID_CSV")
        self.assertEqual(self.controllerobj.validate_csv("Sample_valid.csv"), "VALID_CSV")
        self.assertEqual(self.controllerobj.validate_csv("Sample_invalid1.csv"), "INVALID_CSV")


    def test_send_csv(self):
        self.assertEqual(self.controllerobj.validate_csv("Sample_valid.csv"), "VALID_CSV")
        self.assertEqual(self.controllerobj.send_csv(), "DB_UPDATE_SUCCESSFUL")
        self.assertEqual(self.controllerobj.validate_csv("Sample_valid.xlsx"), "VALID_CSV")
        self.assertEqual(self.controllerobj.send_csv(), "DB_UPDATE_SUCCESSFUL")
        self.assertEqual(self.controllerobj.validate_csv("Sample_invalid2.xlsx"), "INVALID_CSV")
        self.assertEqual(self.controllerobj.send_csv(), "DB_UPDATE_FAILED")
        self.assertEqual(self.controllerobj.validate_csv("Sample_invalid1.xlsx"), "INVALID_CSV")
        self.assertEqual(self.controllerobj.send_csv(), "DB_UPDATE_FAILED")
        self.assertEqual(self.controllerobj.validate_csv("Sample_invalid1.csv"), "INVALID_CSV")
        self.assertEqual(self.controllerobj.send_csv(), "DB_UPDATE_FAILED")

 
if __name__ == '__main__':
    unittest.main()
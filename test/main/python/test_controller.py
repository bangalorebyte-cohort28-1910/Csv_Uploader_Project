import sys, os, unittest
sys.path.insert(1, os.path.dirname('controller.py'))
import src.main.python.controller as controller
import pandas as pd
 
class TestController(unittest.TestCase): 
 
    # def setUp(self):
    #     self.df = pd.read_csv("Sample_valid.csv")


    def test_validateLogin(self):
        self.assertEqual(controller.validate_login('username123', 'password1234'), "INVAID_USERNAME")
        self.assertEqual(controller.validate_login('user123', 'password1234'), "INVALID_PASSWORD")
        self.assertEqual(controller.validate_login('user123', 'password123'), "VALID_USER")

 
    def test_validateCSV(self):
        #self.assertEqual( controller.validate_csv(), True)
        self.assertEqual( controller.validate_csv("Sample_invalid1.xlsx"), "INVALID_CSV")
        self.assertEqual(controller.validate_csv("Sample_invalid2.xlsx"), "INVALID_CSV")
        self.assertEqual(controller.validate_csv("Sample_valid.xlsx"), "VALID_CSV")
        self.assertEqual(controller.validate_csv("Sample_valid.csv"), "VALID_CSV")
        self.assertEqual(controller.validate_csv("Sample_invalid1.csv"), "INVALID_CSV")


    # def test_send_csv(self, self.df):
    #     self.assertEqual(controller.send_csv(self.df), "DB_UPDATE_SUCCESSFUL")
    #     self.assertEqual(controller.send_csv(self.df), "DB_UPDATE_FAILED")
 
if __name__ == '__main__':
    unittest.main()
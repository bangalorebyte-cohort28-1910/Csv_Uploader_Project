import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "controller.py")))

import unittest
# import src.main.python.controller
# from CSV_UPLOADER_PROJECT.src.main.python import controller as ctrl
from src.main.python import controller

 
class TestController(unittest.TestCase):
 
    def setUp(self):
        pass


    def test_validateLogin(self):
        # self.assertEqual( controller.validate_login('username123', 'password1234'), "INVAID_USERNAME")
        # self.assertEqual( controller.validate_login('user123', 'password1234'), "INVALID_PASSWORD")
        # self.assertEqual( controller.validate_login('user123', 'password123'), "VALID_USER")
        self.assertEqual( controller.validate_login('user123', 'password123'), None)
        pass

 
    def test_validateCSV(self):
        pass
        # self.assertEqual( validateCSV, True)
     

    def test_addnums(self):
        # self.assertEqual( ctrl.addnums(3, 4), 7, True)
        self.assertEqual(controller.addnums(3, 4), 7)
 
if __name__ == '__main__':
    unittest.main()
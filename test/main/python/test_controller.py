import sys, os, unittest
sys.path.insert(1, os.path.dirname('controller.py'))
import src.main.python.controller as controller
 
class TestController(unittest.TestCase):
 
    def setUp(self):
        pass


    def test_validateLogin(self):
        self.assertEqual(controller.validate_login('username123', 'password1234'), "INVAID_USERNAME")
        self.assertEqual(controller.validate_login('user123', 'password1234'), "INVALID_PASSWORD")
        self.assertEqual(controller.validate_login('user123', 'password123'), "VALID_USER")
        pass

 
    def test_validateCSV(self):
        # self.assertEqual( validateCSV, True)
        pass
     

    def test_addnums(self):
        # self.assertEqual( ctrl.addnums(3, 4), 7, True)
        self.assertEqual(controller.addnums(3, 4), 7)
 
if __name__ == '__main__':
    unittest.main()
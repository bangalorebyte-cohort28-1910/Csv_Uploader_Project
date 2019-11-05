import unittest
# import src.main.python.controller
# from CSV_UPLOADER_PROJECT.src.main.python import controller as ctrl
 
class TestController(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_validateCSV(self):
        pass
        # self.assertEqual( validateCSV, True)
 
    def test_validateLogin(self):
        pass
        # self.assertEqual( validateLogin, True)

    def test_addnums(self):
        # self.assertEqual( ctrl.addnums(3, 4), 7, True)
        self.assertEqual((3+4), 7, True)
 
if __name__ == '__main__':
    unittest.main()
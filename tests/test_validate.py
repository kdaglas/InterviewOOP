import unittest
from validate import validate_password

class Test_Validation(unittest.TestCase):

    def setUp(self):
        self.valid_password = "ABd1234@1"
        self.invalid_password = "daglas@256"

    
    def test_invalid_password(self):
        resp = validate_password(self.invalid_password)
        self.assertEqual(resp, False)  


    def test_valid_password(self):
        resp = validate_password(self.valid_password)
        self.assertEqual(resp, True)
           
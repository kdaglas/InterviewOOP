import unittest
from ..views import add_new_user


class Test_Views(unittest.TestCase):

    def setUp(self):
        self.username = "Douglas"
        self.password = "ABd1234@1"
        self.the_users = [{"username":"Douglas", "password":"ABd1234@1"}]
        

    def test_register(self):
        resp =  add_new_user(self.username, self.password)
        self.assertEqual(resp, True)

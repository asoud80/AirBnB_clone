#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_instance(self):
        usr = User()
        self.assertIsInstance(usr, User)

    def test_attribute_types(self):
        usr = User()
        self.assertEqual(type(usr.email), str)
        self.assertEqual(type(usr.password), str)
        self.assertEqual(type(usr.first_name), str)
        self.assertEqual(type(usr.last_name), str)


if __name__ == "__main__":
    unittest.main()

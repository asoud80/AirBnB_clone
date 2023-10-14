#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.city import City


class testCity(unittest.TestCase):
    def test_instance(self):
        cty = City()
        self.assertIsInstance(cty, City)

    def test_attribute_types(self):
        cty = City()
        self.assertEqual(type(cty.name), str)
        self.assertEqual(type(cty.state_id), str)


if __name__ == '__main__':
    unittest.main()

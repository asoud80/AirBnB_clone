#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.state import State


class testState(unittest.TestCase):
    def test_instance(self):
        stt = State()
        self.assertIsInstance(stt, State)

    def test_attribute_types(self):
        stt = State()
        self.assertEqual(type(stt.name), str)


if __name__ == '__main__':
    unittest.main()

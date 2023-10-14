#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.review import Review


class testReview(unittest.TestCase):
    def test_instance(self):
        rvw = Review()
        self.assertIsInstance(rvw, Review)

    def test_attribute_types(self):
        rvw = Review()
        self.assertEqual(type(rvw.place_id), str)
        self.assertEqual(type(rvw.user_id), str)
        self.assertEqual(type(rvw.text), str)


if __name__ == '__main__':
    unittest.main()

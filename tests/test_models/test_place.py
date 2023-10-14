#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.place import Place


class testPlace(unittest.TestCase):
    def test_instance(self):
        plc = Place()
        self.assertIsInstance(plc, Place)

    def test_attribute_types(self):
        plc = Place()
        self.assertEqual(type(plc.city_id), str)
        self.assertEqual(type(plc.user_id), str)
        self.assertEqual(type(plc.name), str)
        self.assertEqual(type(plc.description), str)
        self.assertEqual(type(plc.number_rooms), int)
        self.assertEqual(type(plc.number_bathrooms), int)
        self.assertEqual(type(plc.max_guest), int)
        self.assertEqual(type(plc.price_by_night), int)
        self.assertEqual(type(plc.latitude), float)
        self.assertEqual(type(plc.longitude), float)
        self.assertEqual(type(plc.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()

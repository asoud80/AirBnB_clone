#!/usr/bin/python3
"""Unit Testing The BaseModel Class"""
import unittest
import json
from datetime import datetime
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from time import sleep


class TestBaseClass(unittest.TestCase):
    """Base Class Test Module"""

    def setUp(self):
        """ condition to test file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys created file """
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_isinstance(self):
        """ Check if object is basemodel instance """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_id_type(self):
        """ Test id type"""
        bm = BaseModel()
        self.assertEqual(type(bm.id), str)

    def test_datetime_type(self):
        """ Test datetime type """
        bm = BaseModel()
        self.assertEqual(type(bm.created_at), datetime)

    def test_str(self):
        """ Test str output """
        bm = BaseModel()
        self.assertEqual(bm.__str__(), "[" + bm.__class__.__name__ + "]"
                         " (" + bm.id + ") " + str(bm.__dict__))

    def test_id_unique(self):
        """ check for module documentation """
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm3 = BaseModel()
        self.assertTrue((bm1.id != bm2.id) and (bm1.id != bm3.id))
        self.assertTrue((bm2.id != bm1.id) and (bm2.id != bm3.id))
        self.assertTrue((bm3.id != bm1.id) and (bm3.id != bm2.id))

    def test_to_dict(self):
        """testing to dict function"""
        bm = BaseModel()
        dic = bm.to_dict()
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(type(bm.created_at), datetime)
        self.assertEqual(type(bm.updated_at), datetime)
        self.assertEqual(dic["created_at"], bm.created_at.isoformat())
        self.assertEqual(dic["updated_at"], bm.updated_at.isoformat())

    def test_base_from_dict(self):
        """Testing task 4, with kwargs init"""
        bm = BaseModel()
        bmjson = bm.to_dict()
        newbm = BaseModel(**bmjson)
        self.assertEqual(bmjson, newbm.to_dict())
        self.assertEqual(type(newbm.id), str)
        self.assertEqual(type(newbm.created_at), datetime)
        self.assertEqual(type(newbm.updated_at), datetime)

    def test_base_from_emp_dict(self):
        """test with an empty dictionary"""
        dic = {}
        newbm = BaseModel(**dic)
        self.assertEqual(type(newbm.id), str)
        self.assertEqual(type(newbm.created_at), datetime)
        self.assertEqual(type(newbm.updated_at), datetime)

    def test_base_from_non_dict(self):
        """test with a None dictionary"""
        newbm = BaseModel(None)
        self.assertEqual(type(newbm.id), str)
        self.assertEqual(type(newbm.created_at), datetime)
        self.assertEqual(type(newbm.updated_at), datetime)

    def test_save(self):
        """ test save method of basemodel """
        newbm = BaseModel()
        oldtime = newbm.updated_at
        newbm.save()
        newtime = newbm.updated_at
        self.assertLess(oldtime, newtime)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unit testing the file storage class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from models import storage


class TestFileStorageClass(unittest.TestCase):
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

    def test_all(self):
        """ Test method all from filestorage """
        my_obj = FileStorage()
        my_dict = my_obj.all()
        self.assertEqual(type(my_dict), dict)

    def test_new(self):
        """ Tests method new for filestorage """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict = my_obj.all()
        key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertTrue(key in my_dict)

    def test_empty_reload(self):
        """ Empty reload function """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_obj.save()
        my_dict1 = my_obj.all()
        os.remove("test.json")
        my_obj.reload()
        my_dict2 = my_obj.all()
        self.assertTrue(my_dict2 == my_dict1)

    def test_save(self):
        """ Tests the save method for filestorage """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict1 = my_obj.all()
        my_obj.save()
        my_obj.reload()
        my_dict2 = my_obj.all()
        for key in my_dict1:
            key1 = key
        for key in my_dict2:
            key2 = key
        self.assertEqual(my_dict1[key1].to_dict(), my_dict2[key2].to_dict())

    def test_instance(self):
        """ Check storage """
        self.assertIsInstance(storage, FileStorage)


if __name__ == '__main__':
    unittest.main()

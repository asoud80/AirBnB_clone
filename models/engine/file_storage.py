#!/usr/bin/python3
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        newname = obj.__class__.__name__
        newid = obj.id
        newkey = newname + "." + newid
        FileStorage.__objects[newkey] = obj

    def save(self):
        instdic = {}
        for key in FileStorage.__objects:
            instdic[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            json.dump(instdic, fp)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        reloaddic = {"BaseModel": BaseModel, "User": User, "State": State,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}
        if os.path.exists(FileStorage.__file_path) is False:
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fp:
            objs = json.load(fp)
            # clear existing objects
            FileStorage.__objects = {}
            for key in objs:
                # extract class name (since its: classname.id)
                name = key.split(".")[0]
                # create instance of the class using **kwargs
                FileStorage.__objects[key] = reloaddic[name](**objs[key])

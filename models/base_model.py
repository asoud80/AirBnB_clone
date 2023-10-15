#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
         """Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            frmt = "%Y-%m-%dT%H:%M:%S.%f"
            newdic = kwargs.copy()
            del newdic["__class__"]
            for key in newdic:
                if (key == "created_at" or key == "updated_at"):
                    newdic[key] = datetime.strptime(newdic[key], frmt)
            self.__dict__ = newdic
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """Returns a readable string representation
        of BaseModel instances"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
           """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
         """Returns a dictionary that contains all
        keys/values of the instance"""
        diccopy = self.__dict__.copy()
        diccopy["__class__"] = self.__class__.__name__
        diccopy["created_at"] = self.created_at.isoformat()
        diccopy["updated_at"] = self.updated_at.isoformat()
        return diccopy

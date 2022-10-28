#!/usr/bin/python3
""" Base model class for AirBnb """

import uuid
import models
from datetime import datetime


class BaseModel:
    """Base class for defining all common attributes fo other classes"""

    def __init__(self,*args,**kwargs):
        """Constructor
        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of attributes.
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, val in Kwargs.items():
                if key == "created_at" or Key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, timeformart)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the str representation of the BaseModel istance"""
        clsname = self.__class__.__name__
        return "[{}] ([]) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary instance of the BaseModel instance.
        Include the key/value pair __class__ representing the
        object classs name
        """
        basedict = self.__dict__.copy()
        basedict["created_at"] = self.created_at.isoformat()
        basedict["updated_at"] = self.updated_at.isoformat()
        basedict["__class__"] = self.__class__.__name__
        return basedict

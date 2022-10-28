#!/usr/bin/puthon3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Represent an abstracted storage engine
    Attributes:
        __file_path (str): File name
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objclsname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objclsname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file path."""
        objdict = FileStorage.__objects
        objdict_item = {obj: objdict[obj].to_dict() for obj in objdict.keys()}
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dumps(objdict_item, f)

    def reload(self):
        """Deserialize the json file __file_path to __objects,
        if it exists
        """
        try:
            with open(FileStorage.__file_path, "r",encoding="UTF-8") as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

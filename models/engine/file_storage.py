#!/usr/bin/python3
"""Write a class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class FileStorage:
    """this is the class FileStorage"""
    __file_path = "file.json"
    __objects =  {}

    def all (self):
        """returns the dictionar __objects"""
        return FileStorage.__objects
    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)"""
        objects = FileStorage.__objects
        obj_dict = {}
        for obj in objects.keys():
            obj_dict[obj] = objects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)
    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        claas = eval(class_name)
                        instance = claas(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
        


#!/usr/bin/python3
"""This module defines a class to manage file storage for AirBnB clone"""

import json

class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            dict = {}
            for key, value in self.__objects.items():
                dict[key] = value.to_dict()
            json.dump(dict, f)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    if class_name == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass

    objects_copy = __objects
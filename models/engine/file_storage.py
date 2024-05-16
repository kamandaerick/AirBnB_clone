#!/usr/bin/python3

import json

"""This module defines a class to manage file storage for AirBnB clone"""
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
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
    objects_copy = __objects
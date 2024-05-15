#!/usr/bin/python3

import json

"""This module defines a class to manage file storage for AirBnB clone"""
class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key, value in FileStorage.__objects.items():
            json_objects[key] = value
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_objects, f)

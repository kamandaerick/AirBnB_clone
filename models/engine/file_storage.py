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
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.city import City
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    if class_name == "User":
                        self.__objects[key] = User(**value)
                    if class_name == "State":
                        self.__objects[key] = State(**value)
                    if class_name == "City":
                        self.__objects[key] = City(**value)
                    if class_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    if class_name == "Place":
                        self.__objects[key] = Place(**value)
                    if class_name == "Review":
                        self.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass

    objects_copy = __objects
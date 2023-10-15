#!/usr/bin/python3
"""This module defines the storage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary __Ojects"""
        return FileStorage.__objects

    def new(self, obj: BaseModel):
        """
        Sets a new objects
        In __objects the obj with key <obj class name>.id
        """
        k = f"{obj.get_name()}.{obj.id}"
        FileStorage.__objects[k] = obj

    def save(self):
        """Serialzies __objects to a json"""

        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as fp:
            json.dump(obj_dict, fp)

    def reload(self):
        """Deserializes a json file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as user_file:
                data = json.load(user_file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_data = value
                    obj = globals()[class_name](**obj_data)
                    FileStorage.__objects[key] = obj

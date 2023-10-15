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
        return self.__objects

    def new(self, obj: BaseModel):
        """
        Sets a new objects
        In __objects the obj with key <obj class name>.id
        """
        k = f"{obj.get_name()}.{obj.id}"
        self.__objects[k] = obj.to_dict()

    def save(self):
        """Serialzies __objects to a json"""
        json_object = json.dumps(self.__objects)

        with open(self.__file_path, 'w') as fp:
            fp.write(json_object)

    def reload(self):
        """Deserializes a json file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as user_file:
                self.__objects = json.load(user_file)

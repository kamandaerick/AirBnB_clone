#!/usr/bin/python3
"""This module creates the base class BaseModel"""
import uuid
from datetime import datetime


class BaseModel(object):

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BAseModel class.
        Generate a unique ID, set creation and updation time
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a human readable string representation of the object
        including class name, ID, and a dictionary of object attributes
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the "updated_at" attribute with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert an object into a dictionary
        Include all instance attributes, class name, and time created
        and updated in isoformat
        Returns a dictionary containing all keyvalues of __dict__ of instance
        """
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()

        return data

#!/usr/bin/python3
"""This module creates the base class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    __fmt_datetime = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs) -> None:
        """Initializes the instance of this class 'BaseModel'"""
        from models import storage  # noqa
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'updated_at' or k == 'created_at':
                        v = datetime.strptime(v, self.__fmt_datetime)
                    # self.__dict__.update({k: v})
                    setattr(self, k, v)

    @classmethod
    def get_name(cls) -> str:
        """Returns the name of the class"""
        return cls.__name__

    def __str__(self) -> str:
        """
        Return a human readable string representation of the object
        including class name, ID, and a dictionary of object attributes
        """
        return f"[{self.get_name()}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Update the "updated_at" attribute with current datetime
        """
        from models import storage  # noqa

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        Convert an object into a dictionary
        Include all instance attributes, class name, and time created
        and updated in isoformat
        Returns a dictionary containing all keyvalues of __dict__ of instance
        """
        d = {}
        d['__class__'] = self.get_name()
        d.update(self.__dict__)
        d['created_at'] = self.created_at.strftime(self.__fmt_datetime)
        d['updated_at'] = self.updated_at.strftime(self.__fmt_datetime)
        return d

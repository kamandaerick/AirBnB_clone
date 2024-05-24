#!/usr/bin/python3
"""Defines a base class for all models in our hbnb clone"""

from datetime import datetime
import uuid
from models import storage
class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Initialize base model"""
        if kwargs:
            for key, value in kwargs.items():
                if not "__class__" in key:
                    setattr(self, key, value)
                    if key == "id":
                        self.id = str(uuid.uuid4())
                    if key == "created_at":
                        self.created_at = datetime.now()
                    if key == "updated_at":
                        self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
#!/usr/bin/python3
from datetime import datetime
import uuid

"""Defines a base class for all models in our hbnb clone"""
class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self):
        """Initialize base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

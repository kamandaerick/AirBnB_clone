#!/usr/bin/python3
"""This module creates a new user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from the class BAseModel"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

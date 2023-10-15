#!/usr/bin/python3
"""This module defines a Clas City"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id: str = ""
    name: str = ""

#!/usr/bin/python3
"""This module defines a class Reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id: str = ""
    user_id: str = ""
    text: str = ""

#!/usr/bin/python3
"""Count instances of each class"""

from models.engine.file_storage import FileStorage
import re

text = ""
for k, v in FileStorage.objects_copy.items():
    text += str(v)

def count_city():
    """Count the number of instances of City"""
    pattern = re.compile(r"\bCity\b")
    matches = pattern.findall(text)
    return len(matches)

def count_user():
    """Count the number of instances of User"""
    pattern = re.compile(r"\bUser\b")
    matches = pattern.findall(text)
    return len(matches)

def count_review():
    """Count the number of instances of Review"""
    pattern = re.compile(r"\bReview\b")
    matches = pattern.findall(text)
    return len(matches)

def count_place():
    """Count the number of instances of Place"""
    pattern = re.compile(r"\bPlace\b")
    matches = pattern.findall(text)
    return len(matches)

def count_amenity():
    """Count the number of instances of Amenity"""
    pattern = re.compile(r"\bAmenity\b")
    matches = pattern.findall(text)
    return len(matches)

def count_state():
    """Count the number of instances of State"""
    pattern = re.compile(r"\bState\b")
    matches = pattern.findall(text)
    return len(matches)

def count_base_model():
    """Count the number of instances of BaseModel"""
    pattern = re.compile(r"\bBaseModel\b")
    matches = pattern.findall(text)
    return len(matches)

def all_instances():
    """Count the number of instances of all classes"""
    return count_city() + count_user() + count_review() + count_place() + count_amenity() + count_state() + count_base_model()

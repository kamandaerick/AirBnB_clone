#!/usr/bin/python3
"""Create an instance for FileStorage and reload"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
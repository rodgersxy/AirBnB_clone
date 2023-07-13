#!/usr/bin/python3
"""
For creating instance for FileStorage class
and reloading the data from the JSON file.
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

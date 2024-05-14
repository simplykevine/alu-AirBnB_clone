#!/usr/bin/python3
"""This script initializes the package.It imports the FileStorage class from the
models.engine.file_storage module, creates an instance
of FileStorage called 'storage', and reloads the stored data.
"""
from models.engine import storage

def reload():
    storage.reload()
    storage = FileStorage()


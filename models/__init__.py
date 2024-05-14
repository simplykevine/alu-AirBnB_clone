#!/usr/bin/python3
"""
This script initializes the package.
It imports the FileStorage class from the
models.engine.file_storage module, creates an instance
of FileStorage called 'storage', and reloads the stored data.

Note: Please ensure your comments follow the PEP 8 style
guide for readability and consistency.
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

#!/usr/bin/python3
"""__init__magic method for models directory"""
from models.engine.file_storage import FileStorage

'''create a unique FileStorage instance for the application'''
from models.engine.file_storage import FileStorage


'''A variable storage, an instance of FileStorage'''
storage = FileStorage()
storage.reload()

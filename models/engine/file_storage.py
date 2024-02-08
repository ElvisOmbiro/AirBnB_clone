#!/usr/bin/python3
import os
import json

class FileStorage():
    """Class that takes care of storage of objects in JSON"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a new object in __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialises __objects to the JSON file path"""
        #if os.path.exists(FileStorage.__file_path):
        print("In here")
        d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """Deserialises __objects from the JSON file path"""
        #if os.path.exists(FileStorage.__file_path):
        from ..base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                dict_data = json.load(f)
                for k, v in dict_data.items():
                    class_name = eval(v["__class__"])
                    FileStorage.__objects[k] = class_name(**v)
        except FileNotFoundError:
            pass

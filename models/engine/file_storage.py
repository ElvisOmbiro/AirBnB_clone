#!/usr/bin/python3
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
        d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """Deserialises __objects from the JSON FileStorage
        This method runs everytime the console starts up
        """

        from ..base_model import BaseModel
        #from ..amenity import Amenity
        #from ..city import City
        #from ..place import Place
        #from ..review import Review
        #from ..state import State
        #from ..user import User

        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                dict_data = json.load(f)
                for k, v in dict_data.items():
                    class_name = eval(v["__class__"])
                    FileStorage.__objects[k] = class_name(**v)
        except FileNotFoundError:
            pass

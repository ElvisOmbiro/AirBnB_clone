#!/usr/bin/python3
import os
import json

class FileStorage():
    """Class that takes care of storage of objects in JSON"""
    __file_path = ""
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets a new object in __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects.update({key: obj.to_dict()})

    def save(self):
        """Serialises __objects to the JSON file path"""
        #self.__file_path = self.__class__.__name__ + ".json"
        if os.path.exists(self.__file_path):
            #with open(self.__file_path, 'w+') as json_file:
            print("Saving")
            with open(self.__file_path, 'w') as json_file:
                json.dump(self.__objects, json_file, indent=2)
                print("Saved")

    def reload(self):
        """Deserialises __objects from the JSON file path"""
        #self.__file_path = self.__class__.__name__ + ".json"
        if os.path.exists(self.__file_path):
            #with open(self.__file_path, 'r') as json_file:
            print("Loading")
            with open(self.__file_path, 'r') as json_file:
                self.__objects = json.load(json_file)
                print("Loaded")

#!/usr/bin/python3

import unittest
import os
import ...models.base_model.BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """Test cases for class FileStorage"""
    def setUp(self):
        """Initialises instances before every test"""
        self.model1 = BaseModel()
        dictA = {"name": "Jane Doe", "Car": "Buick"}
        self.model2 = BaseModel(**dictA)
        self.model3 = User()
        self.model4 = Place()
        self.model5 = Review()
        self.model6 = State()

    def tearDown(self):
        """Deletes instances after every test"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Objects(self):
        """Test whether raw python storage ditionary works"""
        self.assertTrue(len(FileStorage._FileStorage__objects) > 0)
        for key in FileStorage._FileStorage__objects.keys():
            args = key.split(".")
            if args[0] == "BaseModel":
                self.assertEqual(FileStorage._FileStorage__objects[key],
                                 self.model1.to_dict() or self.model2.to_dict
                                 ())
        self.assertEqual(FileStorage._FileStorage__objects,
                         FileStorage.all())

    def test_Reload(self):
        """Tests the reload function"""
        FileStorage.reload()
        loaded_objs = FileStorage.all()
        loaded_model = loaded_objs[f"{model.__class__.__name__}.{model.id}"]
        self.assertGreater(loaded_model.updated_at, model.updated_at)


if __name__ == "__main__":
    unittest.main()

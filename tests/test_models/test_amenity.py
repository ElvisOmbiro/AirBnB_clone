#!/usr/bin/python3

import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(clss):
        clss.amenity2 = Amenity()
        clss.amenity2.name = "Washing machine"

    @classmethod
    def tearDownClass(clss):
        del clss.amenity2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        r = style.check_files(['models/amenity.py'])
        self.assertEqual(r.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(me), str)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity2.__dict__)
        self.assertTrue('created_at' in self.amenity2.__dict__)
        self.assertTrue('updated_at' in self.amenity2.__dict__)
        self.assertTrue('name' in self.amenity2.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.amenity2.name), str)

    def test_save(self):
        self.amenity2.save()
        self.assertNotEqual(self.amenity2.created_at, self.amenity2.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity2), True)


if __name__ == "__main__":
    unittest.main()

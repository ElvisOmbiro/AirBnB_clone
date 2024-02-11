#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cyi = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cyi))
        self.assertNotIn("state_id", cyi.__dict__)

    def test_name_is_public_class_attribute(self):
        cyi = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cyi))
        self.assertNotIn("name", cyi.__dict__)

    def test_two_cities_unique_ids(self):
        ct1 = City()
        ct2 = City()
        self.assertNotEqual(ct1.id, ct2.id)

    def test_two_cities_different_created_at(self):
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertLess(ct1.created_at, ct2.created_at)

    def test_two_cities_different_updated_at(self):
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertLess(ct1.updated_at, ct2.updated_at)

    def test_str_representation(self):
        dat = datetime.today()
        dat_repre = repr(dat)
        cyi = City()
        cyi.id = "123456"
        cyi.created_at = cyi.updated_at = dat
        cystr = cyi.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dat_repre, cystr)
        self.assertIn("'updated_at': " + dat_repre, cystr)
    def test_args_unused(self):
        cyi = City(None)
        self.assertNotIn(None, cyi.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dat = datetime.today()
        dat_iso = dat.isoformat()
        cyi = City(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(cyi.id, "345")
        self.assertEqual(cyi.created_at, dat)
        self.assertEqual(cyi.updated_at, dat)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        cyi = City()
        sleep(0.05)
        first_updated_at = cyi.updated_at
        cyi.save()
        self.assertLess(first_updated_at, cyi.updated_at)

    def test_two_saves(self):
        cyi = City()
        sleep(0.05)
        first_updated_at = cyi.updated_at
        cyi.save()
        second_updated_at = cyi.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cyi.save()
        self.assertLess(second_updated_at, cyi.updated_at)

    def test_save_with_arg(self):
        cyi = City()
        with self.assertRaises(TypeError):
            cyi.save(None)

    def test_save_updates_file(self):
        cyi = City()
        cyi.save()
        cyid = "City." + cyi.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        cyi = City()
        self.assertIn("id", cyi.to_dict())
        self.assertIn("created_at", cyi.to_dict())
        self.assertIn("updated_at", cyi.to_dict())
        self.assertIn("__class__", cyi.to_dict())

    def test_to_dict_contains_added_attributes(self):
        cyi = City()
        cyi.middle_name = "Holberton"
        cyi.my_number = 98
        self.assertEqual("Holberton", cyi.middle_name)
        self.assertIn("my_number", cyi.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        cyi = City()
        cyi_dict = cyi.to_dict()
        self.assertEqual(str, type(cyi_dict["id"]))
        self.assertEqual(str, type(cyi_dict["created_at"]))
        self.assertEqual(str, type(cyi_dict["updated_at"]))

    def test_to_dict_output(self):
        dat = datetime.today()
        cyi = City()
        cyi.id = "123456"
        cyi.created_at = cyi.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(cyi.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        cyi = City()
        self.assertNotEqual(cyi.to_dict(), cyi.__dict__)

    def test_to_dict_with_arg(self):
        cyi = City()
        with self.assertRaises(TypeError):
            cyi.to_dict(None)


if __name__ == "__main__":
    unittest.main()

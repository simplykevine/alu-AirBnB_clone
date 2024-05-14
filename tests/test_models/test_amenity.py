#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of
    the Amenity class.
    """

    def test_no_args_instantiates(self):
        """
        Test that Amenity class can be instantiated
        with no arguments.
        """
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new instance of Amenity is
        stored in the 'objects' attribute.
        """
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute of Amenity is of type str."""
        self.assertEqual(str, type(Amenity().id))

    # ... (similar comments for other test methods)

    def test_instantiation_with_None_kwargs(self):
        """
        Test that instantiation with None kwargs raises TypeError.
        """
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """
    Unittests for testing save method of the Amenity class.
    """

    @classmethod
    def setUp(self):
        """
        Set up test environment by renaming 'file.json' to 'tmp'.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """
        Clean up test environment by removing 'file.json' and
        renaming 'tmp' back.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """
        Test that the save method updates the 'updated_at'
        attribute
        ."""
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    # ... (similar comments for other test methods)

    def test_save_with_arg(self):
        """Test that save method with an argument raises TypeError."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        """
        Test that save method updates the 'file.json' with
        Amenity instance information.
        """
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """Test that to_dict method returns a dictionary."""
        self.assertTrue(dict, type(Amenity().to_dict()))

    # ... (similar comments for other test methods)

    def test_to_dict_with_arg(self):
        """Test that to_dict with an argument raises TypeError."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()

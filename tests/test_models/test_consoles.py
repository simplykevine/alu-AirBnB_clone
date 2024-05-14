#!/usr/bin/python3
"""Unit tests for the console (command interpreter) module."""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand class."""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Test the create command using FileStorage.

        Checks if the create command successfully creates instances
        and stores them in the FileStorage.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            console = HBNBCommand()
            console.onecmd('create City name="Texas"')
            model_id = cout.getvalue().strip()
            clear_stream(cout)

            # Check if instance is stored in FileStorage
            self.assertIn('City.{}'.format(model_id), storage.all().keys())

            console.onecmd('show City {}'.format(model_id))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())
            clear_stream(cout)

            console.onecmd('create User name="James" age=17 height=5.9')
            model_id = cout.getvalue().strip()
            self.assertIn('User.{}'.format(model_id), storage.all().keys())
            clear_stream(cout)

            console.onecmd('show User {}'.format(model_id))
            self.assertIn("'name': 'James'", cout.getvalue().strip())
            self.assertIn("'age': 17", cout.getvalue().strip())
            self.assertIn("'height': 5.9", cout.getvalue().strip())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        """Test the create command using Database Storage.

        Checks if the create command successfully creates instances
        and stores them in the Database Storage.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            console = HBNBCommand()

            # Raise an exception if creating User instance with missing attributes
            with self.assertRaises(sqlalchemy.exc.OperationalError):
                console.onecmd('create User')
            clear_stream(cout)

            console.onecmd('create User email="john25@gmail.com" password="123"')
            model_id = cout.getvalue().strip()

            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(model_id))
            result = cursor.fetchone()

            # Check if instance is stored in Database Storage
            self.assertTrue(result is not None)
            self.assertIn('john25@gmail.com', result)
            self.assertIn('123', result)
            cursor.close()
            dbc.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_show(self):
        """Test the show command using Database Storage.

        Checks if the show command successfully retrieves instances
        from the Database Storage.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            console = HBNBCommand()
            user = User(email="john25@gmail.com", password="123")
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(user.id))
            result = cursor.fetchone()

            # Check if instance is not found before saving
            self.assertTrue(result is None)
            console.onecmd('show User {}'.format(user.id))
            self.assertEqual(cout.getvalue().strip(), '** no instance found **')

            user.save()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(user.id))
            clear_stream(cout)
            console.onecmd('show User {}'.format(user.id))
            result = cursor.fetchone()

            # Check if instance is retrieved from Database Storage
            self.assertTrue(result is not None)
            self.assertIn('john25@gmail.com', result)
            self.assertIn('123', result)
            self.assertIn('john25@gmail.com', cout.getvalue())
            self.assertIn('123', cout.getvalue())
            cursor.close()
            dbc.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_count(self):
        """Test the count command using Database Storage.

        Checks if the count command returns the correct count of
        instances in the Database Storage.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            console = HBNBCommand()
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT COUNT(*) FROM states;')
            res = cursor.fetchone()
            prev_count = int(res[0])

            console.onecmd('create State name="Enugu"')
            clear_stream(cout)
            console.onecmd('count State')
            cnt = cout.getvalue().strip()

            # Check if count is incremented by 1
            self.assertEqual(int(cnt), prev_count + 1)
            clear_stream(cout)

            console.onecmd('count State')
            cursor.close()
            dbc.close()

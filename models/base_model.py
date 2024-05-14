#!/usr/bin/python3
"""
Base model defining common attributes/
methods for other classes

"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class inherited by other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Official string representation.

        Returns:
            str: Formatted string containing class name, instance id,
            and attributes.
        """

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__.

        Returns:
            dict: Dictionary containing instance attributes.
        """

        my_dict = self.__dict__.copy()
        my_dict["_class"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

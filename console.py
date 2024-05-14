#!/usr/bin/python3
"""
This module contains the entry point for the command interpreter.
"""

import cmd
from models import storage
from models.engine.errors import *
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import inspect
import shlex
import json
import sys


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.

    commands:
    quit - exit the program
    EOF - exit the program
    """

    prompt = '(hbnb) '
    classes = {"Amenity": Amenity, "BaseModel": BaseModel,
               "City": City, "Place": Place, "Review": Review,
               "State": State, "User": User}

    def emptyline(self):
        """
        Overrides the default emptyline method to do nothing
        """
        pass

    def do_create(self, args):
        '''
        Creates and saves a new object
        ex: create BaseModel
        '''
        if not args:
            print("**class name missing**")
        elif args not in self.classes:
            print("**class doesn't exist**")
        else:
            new_instance = self.classes[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        '''
        Shows the dict representation of an object
        ex: show BaseModel 12345
        '''
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    print(all_objs[key])

    def do_destroy(self, args):
        '''
        Deletes an object
        based on its class and id
        ex: destroy BaseModel 1234567
        '''
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    del all_objs[key]
                    FileStorage().save()

    def do_all(self, args):
        '''
        Shows all objects in storage or all objects of a certain class
        ex: all
        or
        ex: all BaseModel
        '''
        all_objs = FileStorage().all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            class_objs = {k: v for k, v in all_objs.items() if args in k}
            print([str(obj) for obj in class_objs.values()])

    def do_update(self, args):
        """
        Update an object by add or updating an attribute
        ex: update BaseModel 1234-1234-1234 email "username@email.com"
        """
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                elif len(args_list) < 3:
                    print("** attribute name missing **")
                elif len(args_list) < 4:
                    print("** value missing **")
                else:
                    obj = all_objs[key]
                    setattr(obj, args_list[2], eval(args_list[3]))
                    obj.save()

    def do_count(self, args):
        """
        Return the number of instance of a class
        """
        if not args:
            print("** class name missing **")
        else:
            class_objs = {
                k: v for k,
                v in FileStorage().all().items() if args in k}
            print(len(class_objs))

    def do_quit(self, args):
        """
        Exit the program.
        """
        print("Goodbye!")
        return True

    def do_EOF(self, args):
        """
        (Ctrl+D or Ctrl+Z) EOF signal to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

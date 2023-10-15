#!/usr/bin/python3
"""An interpreter for my AirBnB clone commands"""
import cmd
import sys
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from typing import Dict

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        sys.exit()

    def do_EOF(self, args):
        """EOF command to quit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel and save to JSON"""
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args)
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print the string representation of an
        instance based on class name and id"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        try:
            cls = eval(args_list[0])
            instance = storage.get(cls, args_list[1])
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Destroys an object"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        try:
            cls = eval(args_list[0])
            instance = storage.get(cls, args_list[1])
            if instance:
                storage.delete(instance)
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Print all string representation of all instances
        based or not on the class name"""
        args_list = args.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args_list[0] in classes:
            cls = eval(args_list[0])
            print([str(obj) for obj in cls.all().values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update an instance based on the class name and id
         by adding or updating attribute (save change into json)
         """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        if len(args_list) < 4:
            print("** value missing **")
            return
        try:
            cls = eval(args_list[0])
            instance = storage.get(cls, args_list[1])
            if instance:
                attr_name = args_list[2]
                attr_value = args_list[3]
                try:
                    attr_value = eval(attr_value)
                except (NameError, SyntaxError):
                    pass
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

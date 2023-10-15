#!/usr/bin/python3
"""An interpreter for my AirBnB clone commands"""
import cmd
import sys

from typing import Dict

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

        if not arg:
            print("** class name missing **")
            return
        try:
            new_user = User()
            for pair in arg.split(','):
                key, value = [part.strip() for part in pair.split('=')]
                setattr(new_user, key, value)
            new_user.save()
            print(new_user.id)
        except Exception as e:
            print(e)

    def do_show(self, args):
        """Print the string representation of an
        instance based on class name and id"""

        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, obj_id = arg.split(' ')
            obj = storage.all().get(f'{class_name}.{obj_id}')
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_destroy(self, args):
        """Destroys an object"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]
        if f"{class_name}.{obj_id}" not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[f"{class_name}.{obj_id}"]
        storage.save()

    def do_all(self, args):
        """Print all string representation of all instances
        based or not on the class name"""

        class_name = arg if arg else None
        obj_list = []

        for key, value in storage.all().items():
            if class_name is None or key.split('.')[0] == class_name:
                obj_list.append(str(value))

        if obj_list:
            print(obj_list)
        else:
            print("** no instances found **")

    def do_update(self, args):
        """Update an instance based on the class name and id
         by adding or updating attribute (save change into json)
         """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]
        if f"{class_name}.{obj_id}" not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute = args[2]
        value = args[3]

        obj = storage.all()[f"{class_name}.{obj_id}"]
        setattr(obj, attribute, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

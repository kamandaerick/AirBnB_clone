#!/usr/bin/python3
"""This is a commandline interpreter for commands specific to the AirBnB project"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """Quit the console"""
        return True
    def help_EOF(self):
        """A function that provides information on the EOF command"""
        print("Quit command to exit the program")

    do_quit = do_EOF
    help_quit = help_EOF

    """PROJECT-RELATED COMMANDS"""
    def do_create(self, line):
        """Create a new instance of BaseModel and save it to JSON file and Print its id"""
        if not line:
            print("** class name missing **")
        elif line not in globals():
            print("** class doesn't exist **")
        else:
            model_class = globals()[line]
            instance = model_class()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Print the string representation of an instance based on the class name and id"""
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        elif tokens[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        instance_attribute = f"{tokens[0]}.{tokens[1]}"
        if instance_attribute not in FileStorage.objects_copy:
            print("** no instance found **")
        instance = FileStorage.objects_copy[instance_attribute]
        print(instance)
if __name__ == '__main__':
    HBNBCommand().cmdloop()